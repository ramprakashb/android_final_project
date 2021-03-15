#!/usr/bin/python3
# -----------------------------
# Date: Mon March 1 13:34
# Author: nnikolov3 (GitHub)
# Purpose: Turn LED 0 ON (not the one on
# Explorer HAT
# -----------------------------

import explorerhat as HAT
import RPi.GPIO as GPIO
import sys
import subprocess


# Toggle
def turn_off_led1():
    # HAT.output.one.stop()
    try:
        HAT.output.one.off()
    # Ctrl-C
    except KeyboardInterrupt:
        sys.exit(1)

    # Anything else
    except Exception:
        sys.exit(1)

    finally:
        GPIO.cleanup()
        sys.exit(1)


def main():
    # HAT.output.one.stop()
    # subprocess.run(["kill", "-9", "$(ps | grep 'led1_on.py' | awk '$0')"])
    turn_off_led1()


if __name__ == "__main__":
    # execute only if run as a script
    main()
