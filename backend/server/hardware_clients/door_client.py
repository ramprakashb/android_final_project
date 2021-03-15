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


import re
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import socket
import subprocess
import paho.mqtt.client as mqtt
from time import sleep
import explorerhat as HAT

# -----------


class constants:
    """ Constants """

    HOST = socket.gethostname()
    KEEPALIVE = 60
    CLIENT = mqtt.Client()
    PORT = 1883
    PATH = os.path.dirname(os.path.realpath(__file__))
    WORKER_PATH = PATH + "/../firebase/workers/"


# ---------------------------------------


class Door(object):
    """ Object to update the doorbell """

    # ---------------------------------------
    @staticmethod
    def on_connect(CLIENT):
        """
        Subscribing in on_connect() means that if we lose the connection and
        reconnect then subscriptions will be renewed.
        """
        CLIENT.subscribe("DOOR")
        return

    # ---------------------------------------
    @staticmethod
    def on_subscribe(CLIENT, userdata, mid, granted_qos):
        print("Subscribed")
        return

    # ---------------------------------------

    @staticmethod
    def led1_on():
        print("LED ON ... ")
        return subprocess.run([constants.WORKER_PATH + "led1_on.py"])

    # ---------------------------------------
    @staticmethod
    def led1_off():
        print("LED OFF ... ")
        return subprocess.run([constants.WORKER_PATH + "led1_off.py"])

    # ---------------------------------------
    @staticmethod
    def on_message(CLIENT, userdata, msg):
        payload = str(msg.payload)

        if payload:
            print("Payload received")

        # ---------------------------------------
        is_on = re.compile("Open")
        is_off = re.compile("Closed")

        if str(msg.topic) == "DOOR":
            if is_on.search(payload):
                print("Door Opened ...")
                print("Turning on Led 1 ...")
                Door.led1_on()
            elif is_off.search(payload):
                print("Door Closed ...")
                print("Turning off Led 1 ...")
                Door.led1_off()

        return

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
    if Door.start_deamon() is not True:
        return "Error: Deamon did not start"

    # ---------------------------------------

    # Get the path to JSON file
    script_path = os.path.dirname(os.path.realpath(__file__))

    # Json file name
    file_name = "final-project-backend-firebase-adminsdk-qdyq3-719ba73274.json"

    # Path to configuration file
    config_json = script_path + "/../firebase/private_key/" + file_name

    # Url to database
    database_url = "https://final-project-backend-default-rtdb.firebaseio.com/"

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(config_json)
    # Instantiates a client

    if cred:
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {"databaseURL": database_url})

    door_status_ref = db.reference("DOOR_STATUS")

    # constants.CLIENT.on_connect = Door.on_connect(constants.CLIENT)
    # constants.CLIENT.on_subscribe = Door.on_subscribe
    # constants.CLIENT.on_message = Door.on_message

    print("Here")
    # ---------------------------------------
    while True:
        door_status = door_status_ref.get()
        print(door_status)
        if door_status == "Closed":
            # Door.led1_on()
            HAT.output.one.write(0)
        else:
            # Door.led1_off()
            HAT.output.one.write(1)
        # constants.CLIENT.publish("DOOR", door_status)
        sleep(1.0)

    # ---------------------------------------


if __name__ == "__main__":
    main()
