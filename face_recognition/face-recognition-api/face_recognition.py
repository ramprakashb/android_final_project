#!/usr/bin/python3

"""
Api for triggering the camera,
recognizing if it is a human,
and storing the image.
"""
import cv2
import sys
import os

# --------------------------------


class const:
    """Creating a class
    with constants to ensure that
    the values are immutable
    """

    OS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
    CONFIG_DIR = OS_FILE_DIR + "/../configs/"
    FRONT_FACE_XML = CONFIG_DIR + "haarcascade_frontalface_default.xml"
    CAM_IMAGE_DIR = OS_FILE_DIR + "/../cam-images/"


# --------------------------------
"""
Function to inititizlize camera attached to
Raspberry Pi. Return Error if camera not found
"""
def camInit():
    try:
        vid = cv2.VideoCapture(0)
        status = 0
        pass
    except Exception:
        try:
            vid = cv2.VideoCapture(1)
            status = 0
            pass
        except Exception:
            try:
                vid = cv2.VideoCapture(2)
                status = 0
                pass
            except Exception:
                print("Please Connect Video Camera")
                print("Cam Init Failed")
                status = 1
                return None, status
            pass
        pass
    return vid, status


# --------------------------------
def main():
    # Initialize Camera
    vid, stat = camInit()
    if stat != 0:
        return stat

    # Import Machine learning Model
    try:
        ffCascade = cv2.CascadeClassifier(const.FRONT_FACE_XML)
        pass
    except Exception:
        print("Cascade File Not Found")
        return 3
    # Start Capturing 60 frames and detect human faces
    hCounter = 0
    for i in range(0, 60):
        ret, img = vid.read()
        try:
            # Preprocess the image by converting it to gray scale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except Exception:
            print("Camera not found")
            return 1
        try:
            # Pass the processed image to Machine learning model to detect faces
            # Faces are returned in 2-d array with coordinates of faces detected.
            faces = ffCascade.detectMultiScale(gray, 1.3, 5)
        except Exception:
            print("Cascade not found")
            return 3
        if len(faces) > 0:
            hCounter += 1
            fImage = img
            pass
    cv2.waitKey(1)
    pass
    vid.release()
    cv2.destroyAllWindows()
    possi = (hCounter / 60) * 100

    # Face Detected/ Person Detected
    # 1 for exception 2 for no human
    if possi >= 80.0:
        # Upload or save the image in destined folder
        # Compress Image
        # calculate the 50 percent of original dimensions
        width = int(fImage.shape[1] * 50 / 100)
        height = int(fImage.shape[0] * 50 / 100)
        # resize image
        output = cv2.resize(fImage, (width, height))
        # Try saving to particular folder,
        # if successful, return success else return failed
        try:
            cv2.imwrite(const.CAM_IMAGE_DIR + "face.png", output)
            pass
        except Exception:
            print("Unable to save the file, Directory not found!!!")
            return 4
        pass
    else:
        return 2
    return 0


# --------------------------------

if __name__ == "__main__":
    code = main()
    print(code)
    sys.exit(code)
