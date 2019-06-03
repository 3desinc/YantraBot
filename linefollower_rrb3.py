#!/usr/bin/env python3

import RPi.GPIO as GPIO
from rrb3 import *
from time import sleep
#initialize variables 
voltB = 6 ## number of batteries * 1.5
voltM = 6 ## voltage of motors, standard is 6 volts.

GPIO.setmode(GPIO.BCM)
rr = RRB3(voltB,voltM)

#Use pin 7 for the line follower sensor on RRB3
#The other 2 pins are 3V & G
sensorPin = 7
GPIO.setup(sensorPin,GPIO.IN)

#set up the motors
speed1 = 0.15
speed2 = 0.25
timeout = 100
# If sensorPin return 1 (Black) or returns 0 (White or Grey)
try:
    while(timeout > 0):
        if GPIO.input(sensorPin) == 1:
            # Set motors to go forward, left motor set to speed1 & right to speed2 - Goes LEFT
            rr.set_motors(speed1,0,speed2,0)
            # Check every 10 ms (0.01)
            sleep(0.01)
            timeout = timeout + 2
            if timeout > 100:
                timeout = 100
        else:
            # Set motors to still go forward, left motor set to speed2 & right to speed1 - Goes RIGHT
            rr.set_motors(speed2,0,speed1,0)
            sleep(0.01)
            timeout = timeout -1
        print(GPIO.input(sensorPin))
        # If timeout is Zero, then stop the Robot!
        rr.stop()
    print('done')
    rr.stop()

except KeyboardInterrupt:
    rr.stop()              
