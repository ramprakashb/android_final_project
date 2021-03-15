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
from firebase_admin import db


def set_image_true():
    is_config = project_db_config()
    if is_config is not False:
        image_status_ref = db.reference("IMAGE")
        # Set the doorbell to true
        image_status_ref.set(True)
    else:
        return False

    # Is the new value true
    image = image_status_ref.get()
    if image is True:
        return image

    return False


def main():
    is_image = set_image_true()
    if is_image:
        print("True")
        return True

    return False


if __name__ == "__main__":
    main()
