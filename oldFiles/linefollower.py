import RPi.GPIO as GPIO
from gpiozero import Motor
from time import sleep

GPIO.setmode(GPIO.BCM)

#use pin 7 for the line follower. On the hat it is CE!
sensorPin = 7
GPIO.setup(sensorPin,GPIO.IN)
#set up the motors
motor1 = Motor(17,18)
motor2 = Motor(4,5)
speed1 = 0.25
speed2 = 0.15
timeout = 62
while(timeout > 0):
    if GPIO.input(sensorPin) == 1:
        motor1.forward(speed1)
        motor2.forward(speed2)
        sleep(0.01)
        timeout = timeout + 2
        if timeout > 62:
            timeout = 62
    else:
        motor1.forward(speed2)
        motor2.forward(speed1)
        sleep(0.01)
        timeout = timeout -1
    print(GPIO.input(sensorPin))
print('done')
motor1.forward(0)
motor2.forward(0)               
               
               
               
               
##               