#!/usr/bin/env python3

from rrb3 import *
from time import sleep
import RPi.GPIO as GPIO

rr = RRB3(9,6) # sets up RRB3, 9volts from 6 batteries, and 6v motors

GPIO.setmode(GPIO.BCM) # sets the board state
min_distance = 15 # minimum distance before backing up and changing direction
servoPin = 7 # 7 on the RRB3 board
GPIO.setup(servoPin,GPIO.OUT) # sets up the pin for the servo
servo = GPIO.PWM(servoPin,50) # sets the servo to PWM and 50Hz
servo.start(7.5) # starting duty cycle for the servo

def scan():
    servo.ChangeDutyCycle(2.5) #rotates the servo to 0 degrees
    sleep(0.01) #waits for servo to move
    left = rr.get_distance() # reads from the ultrasonic sensor
    sleep(0.5)
    servo.ChangeDutyCycle(7.5) #rotates the servo to 90 degrees
    sleep(0.01)
    ahead = rr.get_distance()
    sleep(1)
    servo.ChangeDutyCycle(12.5) # rotates the servo to 180 degrees
    sleep(0.01)
    right = rr.get_distance()
    sleep(1)
    if(left > ahead and left > right): # if left is the farthest set it
        farthest = 0
    elif(right > ahead and right > left): # if right is the farthest set it
        farthest = 1
    else: # otherwise is neither, then it says go forwards
        farthest = 2
    print(farthest,left,right,ahead) #prints the distances
    servo.ChangeDutyCycle(7.5) #sets the servo back to 90 degrees(forwards)
    sleep(0.1)
    servo.ChangeDutyCycle(0)
    return farthest

#finds a direction to go by reading the ultrasonic sensor at three
#different angles
def find_direction():
    rr.set_motors(0,0,0,0) # resets the motors
    direction = scan()
    if(direction == 0): # 0 is 0degrees, and to the left
        rr.left(0.65)
    if(direction == 1): # 1 is 90 degrees, and forward
        rr.forward(0.1,0.5)
    if(direction == 2): # 2 is 180 degrees, and to the right
        rr.right(0.65)
dist = rr.get_distance()
lastdist = dist
try:
    while True:
        avgdist = (lastdist + dist) / 2 #averages the last distance and the new distance, to remove outliers
        if(avgdist < min_distance): # if the distance is too close then back up and find a new one
            rr.reverse(1,0.5)
            find_direction()
        #if the distance is close, but not too close then it will just
        #check to see if there's a better direction
        elif(avgdist < min_distance + 5):
            find_direction()
        
        rr.set_motors(0.5,0,0.5,0) #drives forward
        lastdist = dist #saves the last distance, so that it can be used for averaging
        sleep(0.1) # buffer time before trying to use the sensor
        dist = rr.get_distance() # reads a new distance
        print(dist) # prints the new distance
        sleep(0.1)
# Properly cleans up when the script is interupted.
except KeyboardInterrupt:
    servo.stop()
    rr.stop()