import RPi.GPIO as GPIO
from gpiozero import Motor
import time
GPIO.setmode(GPIO.BCM)
#motor setup
motor1 = Motor(27,5) # do not use reverse
motor2 = Motor(17,18) # do not use reverse
speed = 0.4

# ultrasonic sensor setup
TRIG = 6
ECHO = 26
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
#calibration time
time.sleep(2)
#ping function returns a distance in cm
def ping():
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    loops = 0
    while(GPIO.input(ECHO) == 0):
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)
    return distance
while(ping() > 5):
    if(ping() < 15):
        motor1.forward(0)
        motor2.forward(speed)
    else:
        motor1.forward(speed)
        motor2.forward(speed)
    time.sleep(0.01)
    print(ping())
motor1.forward(0)
motor2.forward(0)
GPIO.cleanup()