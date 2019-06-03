import RPi.GPIO as GPIO
from gpiozero import Motor
from time import sleep

GPIO.setmode(GPIO.BCM)

# sensor pin
sensorPin = 7 # CE1
GPIO.setup(sensorPin,GPIO.IN)
#set up the motors
motorRight = Motor(17,18) # do not use reverse 18 is not the actual reverse pin
motorLeft = Motor(27,26) #do not use reverse, 5 is not the actual reverse pin
#Drive each motor for a duration
def drive(left,right,duration):
    motorLeft.forward(left)
    motorRight.forward(right)
    sleep(duration)
#reads the sensor
def readFront():
    return GPIO.input(sensorPin)
#drive forward, and then turn until no object is in front
condition = True
while condition == True:
    timeout = 0
    if readFront() == 1:
        print("forward")
        drive(0.3,0.3,0.01)
    while(readFront() == 0):
        print("detected")
        drive(0,0.0,0.01)
        timeout = timeout +1
        if(timeout > 200):
            condition = False
GPIO.cleanup()
