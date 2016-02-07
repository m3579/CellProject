import RPi.GPIO as GPIO

from endoplasmic_reticulum import *

GPIO.setmode(GPIO.BOARD)
try:
    initForNucleusReading()
    while True:
        reading = getNucleusReading()
        if reading >= 100:
            print("Setting 1")
        elif reading >= 50:
            print("Setting 2")
        elif reading >= 0:
            print("Setting 3")
        
finally:
    GPIO.cleanup()
