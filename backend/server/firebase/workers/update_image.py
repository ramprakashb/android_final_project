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
from pathlib import Path
from google.cloud import storage
import os


def is_image(image_dir):
    image = [entry for entry in os.scandir(image_dir) if entry.is_file()]
    if image:
        print("Image exist")
        return True

    return False


# Update image on the cloud based server
def update_firebase_storage(new_image_path):

    # File Dir
    worker_dir = os.path.dirname(os.path.realpath(__file__))

    # Configuration file
    file_name = "/final-project-backend-a78c9fc0dd44.json"

    # JSON File path
    file_path = worker_dir + file_name

    # Create Storage client
    storage_client = storage.Client(file_path)

    # Our bucket
    bucket = storage_client.bucket("final-project-backend.appspot.com")

    blob = bucket.blob("test.png")

    # Upload file
    blob.upload_from_filename(new_image_path, content_type="image/png")


def get_image():

    # Worker script directory
    worker_dir = os.path.dirname(os.path.realpath(__file__))

    # Path to configuration file`
    image_dir = worker_dir + "/../../../../face_recognition/cam-images/"

    # Validate if there is an image
    image = is_image(image_dir)
    if image is not True:
        return False

    # Set image path
    image_path = Path(image_dir)

    # Get the image file path
    list_of_images = list(image_path.glob("**/*.png"))

    # Get the newest image
    newest_image = max(list_of_images, key=os.path.getctime)

    if newest_image:
        return newest_image

    print("Error: png not found")
    return False


def main():

    newest_image = get_image()
    if newest_image is not False:
        print("Image: OK!")
        update_firebase_storage(newest_image)

    return False


if __name__ == "__main__":
    main()
