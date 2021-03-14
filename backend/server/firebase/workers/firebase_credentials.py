#!/usr/bin/python3.7

"""

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
import firebase_admin
from firebase_admin import credentials
import os


# This is common for all workers
# to avoid adding more code we will
# reference this file and function
def project_db_config():

    # Get the path to JSON file
    script_path = os.path.dirname(os.path.realpath(__file__))

    # Json file name
    file_name = "final-project-backend-firebase-adminsdk-qdyq3-719ba73274.json"

    # Path to configuration file
    config_json = script_path + "/../private_key/" + file_name

    # Url to database
    database_url = "https://final-project-backend-default-rtdb.firebaseio.com/"

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(config_json)

    if cred:
        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {"databaseURL": database_url})
        return True
    else:
        return False
