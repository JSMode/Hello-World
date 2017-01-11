# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
while True:
    if(GPIO.input(17) ==1):
        print “Button 1 pressed”
    if(GPIO.input(18) ==1):
        print “Button 2 pressed”
GPIO.cleanup()
