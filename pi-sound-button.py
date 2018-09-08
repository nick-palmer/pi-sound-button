#!/usr/bin/python
#
# This will play audio clips when the button is pressed. Long press (3+ seconds to shutdown)
# -Audio captured from YouTube using https://www.onlinevideoconverter.com/
# -Button functions adapted from https://github.com/gilyes/pi-shutdown/blob/master/pishutdown.py
# -Run python script on startup https://www.raspberrypi-spy.co.uk/2015/02/how-to-autorun-a-python-script-on-raspberry-pi-boot/
#

import RPi.GPIO as GPIO
import time
import os
import glob
import random
from subprocess import call
from datetime import datetime

shutdownPin = 23
shutdownMinSeconds = 3
buttonPressedTime = None


def random_clip():
    i = random.randint(0,len(clips)-1)
    os.system("aplay " + clips[i])
    
def shutdown():
    os.system("aplay " + directory + "clips/arrivederci.wav")
    call(['shutdown', '-h', 'now'], shell=False)

def startup():
    os.system("aplay " + directory + "clips/buongiorno.wav")

def buttonStateChanged(pin):
    global buttonPressedTime

    if not (GPIO.input(pin)):
        # button is down
        if buttonPressedTime is None:
            buttonPressedTime = datetime.now()
    else:
        # button is up
        if buttonPressedTime is not None:
            elapsed = (datetime.now() - buttonPressedTime).total_seconds()
            buttonPressedTime = None
            if elapsed >= shutdownMinSeconds:
                print("shutdown")
                shutdown()
            else:
                print("play clip")
                random_clip()

GPIO.setmode(GPIO.BCM)
GPIO.setup(shutdownPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# get the directory of the script
directory = os.path.dirname(os.path.abspath(__file__)) + "/"

# get the clip files
clips = glob.glob(directory + "clips/*.wav")

# subscribe to button presses
GPIO.add_event_detect(shutdownPin, GPIO.BOTH, callback=buttonStateChanged)

startup()
while True:
    # sleep to reduce unnecessary CPU usage
    time.sleep(10)
