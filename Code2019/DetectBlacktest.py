#!/usr/bin/env python3
#!/usr/bin/env python3
# Name: Satish Mantripragada
# Course: Introduction to 3D Modeling & Robotics
# Program Name: Sample Detect Black

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
# If sensorPin return 1 (Black) or returns 0 (White or Grey)
try:
    while True:
        if GPIO.input(sensorPin) == 1:
            rr.set_led2(1)
            sleep(0.1)
            print(GPIO.input(sensorPin))
            
        else:
            rr.set_led2(0)
            sleep(0.1)
            # Keep going forward
            print(GPIO.input(sensorPin))        
except:
    print('Done: Robot needs to stop')