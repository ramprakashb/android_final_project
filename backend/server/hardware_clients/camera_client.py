#!/usr/bin/python3.7
""" Date:Sun Feb 28 04:46:27 PM PST 2021
Author: nnikolov3 (GitHub)
Purpose: Keep track of doorbell button
Server: mqtt

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""


from time import sleep
import explorerhat as HAT
import paho.mqtt.client as mqtt
import subprocess
import os
import socket
import door_client

class constants:
    """ Constants """

    HOST = socket.gethostname()
    KEEPALIVE = 60
    CLIENT = mqtt.Client()
    PORT = 1883


# ---------------------------------------


class FaceRecognition(object):
    """ Object to update the doorbell """

    @staticmethod
    def on_connect(CLIENT):
        """
        Subscribing in on_connect() means that if we lose the connection and
        reconnect then subscriptions will be renewed.
        """
        CLIENT.subscribe("$SYS/#")
        return

    # ---------------------------------------
    @staticmethod
    def trigger_camera():

        # Get the path to of this file
        # and navigate to workers
        script_path = os.path.dirname(os.path.realpath(__file__))
        api_offset = "/../../../face_recognition/face-recognition-api/"
        api_path = script_path + api_offset
        script_name = "face_recognition.py"
        script = api_path + script_name
        print(script)

        api = subprocess.run(
            [script],
            # capture_output=True,
            timeout=999,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        exit_code = api.returncode
        print(exit_code)
        if exit_code == 0:
            print("Image is ready to update")
            return True
        else:
            print("Error: Exit code " + exit_code)
            return exit_code

    @staticmethod
    def update_image():
        script_path = os.path.dirname(os.path.realpath(__file__))
        worker_path = script_path + "/../firebase/workers/"
        print(worker_path)
        # Run the update_image worker
        update_image = worker_path + "update_image.py"
        print("Updateing image")
        subprocess.run([update_image], capture_output=True)
        print("========================")
        return True

    # ---------------------------------------
    @staticmethod
    def start_deamon():
        """ establish connection with mqtt"""
        # Consts
        CLIENT = constants.CLIENT
        HOST = constants.HOST
        PORT = constants.PORT
        KEEPALIVE = constants.KEEPALIVE
        CLIENT.connect(HOST, PORT, KEEPALIVE)
        print("Connected")
        # ---------------------------------------
        return True


# Function on bell pressed
def bellChanged(pin):
    print("Here")
    bellStatus = HAT.input.one.read()
    if bellStatus == 1:
        try:
            script_path = os.path.dirname(os.path.realpath(__file__))
            worker_offset = "/../firebase/workers/"
            path = script_path + worker_offset
            print(path)
            worker_name = path + "doorbell_true.py"

            # Update the Doorbell key to true
            # in the Firebase
            subprocess.run([worker_name])

            # Trigger the camera
            camera_status = FaceRecognition.trigger_camera()
            print(camera_status)
            # If the camera returned True
            # Update the Cloud Storage
            # Update Date
            # Update the IMAGE in the DB
            if camera_status is True:
                is_updated = FaceRecognition.update_image()
                print(is_updated)
                if is_updated is True:
                    print("========================")
                    # If people are pressing the button too many times
                    # make sure that it sleeps
                    sleep(10.0)

        except RuntimeError:
            sleep(2.0)

        # Ctrl + C
        except KeyboardInterrupt:
            pass

        # Catches any other exceptions.
        except Exception:
            pass
    else:
        print("Sleeping for 1 sec")
        print("========================")
        sleep(1.0)


def main():

    constants.CLIENT.loop_start()
    if FaceRecognition.start_deamon() is not True:
        return "Error: Deamon did not start"

    print("========================")
    constants.CLIENT.on_connect = FaceRecognition.on_connect(constants.CLIENT)

    # Setup hat input
    HAT.input.one.changed(bellChanged)
    # while True:
    print("Passing Handle to door")
    print("========================")
    door_client.main()
    print("Done Executing")
    sleep(1.0)


if __name__ == "__main__":
    main()
