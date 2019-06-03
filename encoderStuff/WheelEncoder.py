## WheelEncoder.py
## is a library to run wheels from rrb3 with an encoder to keep the wheels about equal.
## three functions provided are wheel(n,Rotate) which accepts a wheel number, and a number of rotations.
## driveRotations(r,maxspeed,minspeed) which will drive the car for a number of motor rotations.
## driveCM(cm,maxspeed,minspeed) will accept a distance in CM and drive approximately that far.
## Written by Martin Dickie for 3DES inc
## last updated on 8/10/18
import time
import RPi.GPIO as GPIO
from rrb3 import *
## radius of waterdrop wheel is 31mm
Encode = [27,18] ## Encoder 1 is on pin 27, Encoder 2 is pin 18
rr = RRB3(7,4.5) ## 9 volts, and motors take up to 6.
GPIO.setmode(GPIO.BCM)
## The right wheel is 0 the left wheel is 1
for encoders in range(0,2): #setup the encoders to be input
    GPIO.setup(Encode[encoders], GPIO.IN, GPIO.PUD_UP)
CurRot = [0,0] # number of current partial rotations kept track of for both wheels
Rotations = [0.0,0.0] # number of whole rotations
Last = [0,0] # last read values
In = [0,0] # what the currently read value is
Running = [1,1] # is the wheel running
speed = 0.2 # default max speed
state = [speed,speed]


def wheel(n,rotate): ## Primary function to keep track of rotations and stop after a certain point.
    n=n-1 ## wheel 1 and wheel 2
   ## print("\nwheel"+str(n+2)+"\n ")
    global CurRot, Running, Rotations, state
    state[n] = speed
    if (Rotations[n] + (CurRot[n]/20.0)) >= rotate:
        state[n] = 0
        rr.set_motors(state[1], 0, state[0], 0)
        Running[n] = 0
    if CurRot[n] == 20:
        Rotations[n] = Rotations[n]+1
        CurRot[n] = 0
    else:
        CurRot[n] = CurRot[n]+ 1

def driveRotations(r=3,maxspeed=0.5,minspeed=0.1): ## main function will call Wheel, accepts number of rotations, max speed, and minimum speed.
    ## Allow the variables to change from inside the function.
    if(r < 0):
        r = r*-1
    if(maxspeed < 0.1):
        maxpeed = 0.1
    if(minspeed < 0.05):
        minspeed = 0.05
    global CurRot, Running, Rotations, speed, counter, state
	## setup the speeds
    speed = maxspeed
    speed2 = minspeed
	## as long as one of the wheels is running then the program will continue
    while (Running[0] or Running[1]):
            rr.set_motors(state[1],0,state[0],0) ## keep the motors running at their pace, to make sure it updates when their status changes
            time.sleep(0.01) ## Add a tiny delay, may work without but also may crash due to trying to do too much
            for n in range(0,2): ## run wheel for both wheels
                In[n] = GPIO.input(Encode[n]) ## In is equal to the current input of the encoder
                if In[n] == 0 and Last[n] == 1: ## rotate the wheel if the encoder read false and true.
                    wheel(n,r)
                Last[n] = In[n] ## last input is stored, to compare if it has already seen the hole or not.
            if (getRotations(1) >= getRotations(0)): ## if the right wheel and left wheel are both around the same number of rotations, continue
                state[0] = speed
            else: ## otherwise slow down
                state[0] = speed2
            if (getRotations(0) >= getRotations(1)):
                state[1] = speed
            else:
                state[1] = speed2
            rr.set_motors(state[1],0,state[0],0) ## update motor speeds
    stop()
    GPIO.cleanup()

def driveCM(cm=50,maxspeed=0.5,minspeed=0.1): ## same as driveRotations but for a distance instead of an amount of rotations.
    ## wheels are 65mm diameter, multiply by pi get approximately 204mm, convert to centimeters and you have roughly 20.4 cm per rotation
    rots = 20.4
    dist = cm/rots
    driveRotations(dist,maxspeed,minspeed)
    
def stop():
    print("Stopping")
    print("motor 0 is right, motor 1 is left")
    printRotations()
    print("Traveled roughly " + str(getRotations(0)*20.4) + " cm")
    rr.stop()
    GPIO.cleanup()
    
def printRotations():
    for n in range (0,2):
        print("Rotations in motor "+str(n)+": " + str(getRotations(n)))
        
def getRotations(i):
    return Rotations[i]+CurRot[i]/20
