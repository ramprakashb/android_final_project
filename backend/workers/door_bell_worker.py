#!/usr/bin/python3.7
"""
Author: nnikolov3 (GitHub)
Purpose: Worker Script to track if the doorbell is triggered
Notes:
    - Class names should normally use the CapWords convention.
    - Please follow the pep8 guidlines
    https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles


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


# Print a welcoming message
print("Worker Thread to keep track of the doorbell")
print("==========================================")


class const:
    """ Constants """

    HOST = "$1"


class DoorBellTracker(object):
    """ Object to update and publish the data """


def main():
    print("Test")


if __name__ == "__main__":
    main()
