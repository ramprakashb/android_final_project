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
from firebase_credentials import project_db_config
from firebase_admin import storage
from google.cloud import storage
import os


client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('bucket-id-here')
# Then do other things...
blob = bucket.get_blob('remote/path/to/file.txt')
print(blob.download_as_string())
blob.upload_from_string('New contents!')
blob2 = bucket.blob('remote/path/storage.txt')
blob2.upload_from_filename(filename='/local/path.txt')





def is_image(image_dir):
    image = [entry for entry in os.scandir(image_dir) if entry.is_file()]
    if image:
        print("Image exist")


def update_image():

    # Worker script directory
    worker_dir = os.path.dirname(os.path.realpath(__file__))

    # Path to configuration file
    image_dir = worker_dir + "/../../face-recognition/cam-images/"

    # Validate if there is an image
    is_image(image_dir)

    is_config = project_db_config()
    if is_config is not False:
        bucket_ref = storage.bucket("cam-image")
        # Set the doorbell to true
        bucket_ref.set("opened")
    else:
        return False

    # Is the new value true
    door = door_ref.get()
    if door == "opened":
        return door

    return False


def main():
    is_door_opened = open_door()
    if is_door_opened == "opened":
        print("opened")
        return True

    return False


if __name__ == "__main__":
    main()
