#!/usr/bin/env python3

import RPi.GPIO as GPIO
from rrb3 import *
from time import sleep
#initialize variables
voltB = 9 ## number of batteries * 1.5
voltM = 6 ## voltage of motors, standard is 6 volts.

GPIO.setmode(GPIO.BCM)
rr = RRB3(voltB,voltM)

#Use pin 8 for the line follower sensor on RRB3
#The other 2 pins are 3V & G
sensorPin = 8
GPIO.setup(sensorPin,GPIO.IN)
speed1 = 0.15
speed2 = 0.4
timeout = 10000
# If sensorPin return 1 (Black) or returns 0 (White or Grey)
try:
    while(timeout > 0):
        if GPIO.input(sensorPin) == 1:
            rr.set_led2(1)
            #Backoff (go reverse) since you hit black. Need to stay in bullpen
            rr.set_motors(speed2,1,speed2,1)
            # Check every 10 ms (0.01)
            sleep(0.01)
            timeout = timeout + 2
            if timeout > 1000:
                timeout = 1000
        else:
            rr.set_led2(0)
            # Keep going forward
            rr.set_motors(speed1,0,speed1,0)
            sleep(0.01)
            timeout = timeout -1
            print(GPIO.input(sensorPin))
        print("Timed out while loop")
        
except KeyboardInterrupt:
    print('Done')
    rr.stop()
except:
    print('Done: Robot needs to stop')
    rr.stop()