import RPi.GPIO as GPIO
from gpiozero import Motor
from time import sleep

GPIO.setmode(GPIO.BCM)

# sensor pins
sensorPin1 = 7 # CE1
sensorPin2 = 8 # CE0
GPIO.setup(sensorPin1,GPIO.IN)

GPIO.setup(sensorPin2,GPIO.IN)
#set up the motors
motorRight = Motor(27,18) # do not use reverse 18 is not the actual reverse pin
motorLeft = Motor(17,5) #do not use reverse, 5 is not the actual reverse pin
#Drive each motor for a duration
def drive(left,right,duration):
    motorLeft.forward(left)
    motorRight.forward(right)
    sleep(duration)
#reads the right light sensor
def readRight():
    print(GPIO.input(sensorPin1))
    return GPIO.input(sensorPin1)
    
#reads the left light sensor
def readLeft():
    print(GPIO.input(sensorPin2))
    return GPIO.input(sensorPin2)
    
#drives forever, and will make turns based on if the light is much stronger in one direction
while True:
    if readRight() > readLeft():
        drive(0.0,0.4,0.1)
    elif readLeft() > readRight():
        drive(0.4,0.0,0.1)
    else:
        drive(0.4,0.4,0.1)
