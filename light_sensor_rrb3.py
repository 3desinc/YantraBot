#!/usr/bin/env python3

from rrb3 import *
import RPi.GPIO as GPIO
from time import sleep
# Initialize variables
voltB = 9 ## number of batteries * 1.5
voltM = 6 ## voltage of motors, standard are 6
rr = RRB3(voltB,voltM)
GPIO.setmode(GPIO.BCM)

# sensor pins LightSensor1, LightSensor2
sensorPin1 = 7
sensorPin2 = 2
GPIO.setup(sensorPin1,GPIO.IN)
GPIO.setup(sensorPin2,GPIO.IN)

#reads the Right light sensor (LightSensor1)
def readRight():
    print(GPIO.input(sensorPin1))
    return GPIO.input(sensorPin1)
    
#reads the Left light sensor (LightSensor2)
def readLeft():
    print(GPIO.input(sensorPin2))
    return GPIO.input(sensorPin2)
    
# Robot drives forever, and will make turns based on if the light is much stronger in one direction
try:
    while True:
        if readRight() > readLeft():
        # Make right turn
            rr.right(0.3,0.5)
        elif readLeft() > readRight():
        #Make left turn
            rr.left(0.3,0.5)
        else:
        # Keep going forward
            rr.forward(0.1,0.7)
except KeyboardInterrupt:
    rr.stop()
    
