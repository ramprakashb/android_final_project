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


class constants:
    """ Constants """

    HOST = socket.gethostname()
    KEEPALIVE = 60
    CLIENT = mqtt.Client()
    PORT = 1883


# ---------------------------------------


class Doorbell(object):
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
    def update_doorbell_status(doorbell_status):
        """
        Get the doorbell status (1 or 0) from the explorer hat
        and update the database
        """
        # Get the path to of this file
        # and navigate to workers
        script_path = os.path.dirname(os.path.realpath(__file__))
        worker_path = script_path + "/../firebase/workers/"

        # If the doorbell is active
        # update the real time database with True
        # using one of the workers
        if doorbell_status is True:
            # Path to worker script
            doorbell_true = worker_path + "doorbell_true.py"
            print("True")
            return subprocess.run([doorbell_true], capture_output=True)

        else:
            print("False")
            doorbell_false = worker_path + "doorbell_false.py"
            return subprocess.run([doorbell_false], capture_output=True)

    # ---------------------------------------

    @staticmethod
    def get_doorbell_status():
        """ Get the readings from the sensor """
        doorbell_status = HAT.input.one.read()
        if doorbell_status == 1:
            return True

        return False

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


def main():

    constants.CLIENT.loop_start()
    if Doorbell.start_deamon() is not True:
        return "Error: Deamon did not start"

    constants.CLIENT.on_connect = Doorbell.on_connect(constants.CLIENT)
    while True:
        doorbell_status = Doorbell.get_doorbell_status()
        if doorbell_status is True:
            try:
                doorbell = Doorbell.update_doorbell_status(True)
                print(doorbell)
                sleep(1.0)

            except RuntimeError as error:
                sleep(1.0)
                continue

            # Ctrl + C
            except KeyboardInterrupt:
                pass

            # Catches any other exceptions.
            except Exception:
                pass

        else:
            Doorbell.update_doorbell_status(False)
            sleep(1.0)


if __name__ == "__main__":
    main()
