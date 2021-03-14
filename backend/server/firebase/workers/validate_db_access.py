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

# Imports
from firebase_admin import db
from firebase_credentials import project_db_config

"""
Initialize the SDK

Once you have created a Firebase project, you can initialize
the SDK with an authorization strategy that combines your
service account file together with Google Application Default
Credentials.

Firebase projects support Google service accounts,
which you can use to call Firebase server APIs from
your app server or trusted environment.
If you're developing code locally or deploying
your application on-premises,
you can use credentials obtained
via this service account to authorize server requests.

To authenticate a service account and authorize it to access
Firebase services, you must generate a private key file in JSON format.

Before you can access the Firebase Realtime Database from a server
using the Firebase Admin SDK, you must authenticate your server
with Firebase. When you authenticate a server, rather than sign
in with a user account's credentials as you would in a client app,
you authenticate with a service account which identifies
your server to Firebase.
"""


def get_credentials():

    # Initialize the configuration
    is_config = project_db_config()
    if is_config is not False:

        # Get server status
        server_status_ref = db.reference("SERVER_STATUS")
        server_status = server_status_ref.get()
    else:
        return False

    if server_status:
        return server_status

    return False


def main():
    is_server = get_credentials()
    # if we are able to register
    # and retrieve data from the server
    # return True
    if is_server:
        print("True")
        return True

    return False


if __name__ == "__main__":
    main()
