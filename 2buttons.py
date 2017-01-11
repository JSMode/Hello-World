#
# Simple 2 button setup for Raspberry Pi
# buttons will repeat print if held down
# refer to 2buttons-singlepress.py for 
# single reading per push, regardless the
# duration of button depression.
# JSMode 2017
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
while True:
    if(GPIO.input(17) ==1):
        print “Button 1 pressed”
    if(GPIO.input(18) ==1):
        print “Button 2 pressed”
    
GPIO.cleanup()
