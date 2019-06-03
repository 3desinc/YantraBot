#!/usr/bin/env python3                                  
## simple_light_sensor.py
## This is an example program designed for 3DES programs
## Writen by Martin Dickie
## this example program will just read a light sensor connected to pin 2 and print either 0 or 1, based on how bright the light is.

import RPi.GPIO as GPIO # brings in the packages for GPIO, GPIO is the way to use pins which are connected to the raspberry pi.

GPIO.setmode(GPIO.BCM) # tells the board to use BCM format which is the numbering on the board that we have
                       # there are other ways to have the pin numbers mapped, but they are usually more confusing
GPIO.setup(2,GPIO.IN) # here GPIO is setting pin 2 to be an input which means we can read values from it. Notice how there's a coma, that coma indicates 
                      # that there is a second option in the perameters. so it's (PIN# , INPUT/OUTPUT)

###################################
#####                         ##### 
#####      basic program      #####
#####                         #####
###################################

print(GPIO.input(2)) # this will print whatever the sensor pin is reading. In this case since the Raspberry pi is only using "digital" pins the value can either be 0 or 1. Some other devices can have "analog" pins which are more sensitive and range from 0 to 1023

## That first area is just to print the input. Next let's try printing the input every second forever

###################################
#####                         ##### 
#####    infinite program     #####
#####                         #####
###################################

try: # when planning to do an infinite loop it's good to tell it to try something and then if there's an exception it will know to stop.
    while True: # while will continue until it is given false, so in this case it will continue forever
                print(GPIO.input(2)) # prints the value of pin 2. Same deal as before, so 1 or 0
                sleep(1) # sleep takes any number of seconds and tells the program to wait that long before continuing.
except KeyboardInterrupt: # this exception will happen on a keyboard interrupt. Normally this is pressing Ctrl + C at the same time while in command prompt.
        GPIO.cleanup() # cleanup will reset all of the values to the correct values
