# wheelEncoder.py
# This program will use encoders on the wheels to keep track of rotations on each and correct as one falls behind
from microbit import *
import time
# motobit class, would be imported but having some issues.
class motobit:
    moto_l = 0x21
    moto_r = 0x20
    moto_on = 0x70
    
    def __init__(self, address=0x59):
        self.ADDR = address
          
    def write16(self, a, b):
        i2c.write(self.ADDR, bytes([a, b]), repeat=False)
    
    # True or False
    def enable(self, pwr):
        if pwr:
            self.write16(0x70, 1)
        else:
            self.write16(0x70, 0)
            
    # 0 for right, 1 for left, speed -127 to 127    
    def set_speed(self, motor, speed):
        motor = motor + 32
        if speed >= 0:
            self.write16(motor, 128 + speed)
        else:
            speed = speed + 127
            self.write16(motor, speed)
    # left and right speeds
    
    def drive(self, left, right):
        self.set_speed(0, right)
        self.set_speed(1, left)

# Variables
car = motobit()  # car is the motobit
global rotations  # rotations is the number of rotations for each wheel, starting at 0
rotations = [0, 0]  # and then incrementing by 5 each 20th of a rotation

global toggle  # keeps track of if a wheel is supposed to be on or off
toggle = [1, 1]

global speed1  # speed1 is the primary speed,
global speed2  # and speed 2 is the lower speed

global In  # in and last are the input and the last loops input, this is used
In = [0, 0]  # to check if the wheel has moved at all or not
global last  # it will be 1 or 0 if there is a slot in the encoder, and the other value when there is no slot.
last = [0, 0]

global encode  # the encoder pins, here pin15 is right, and pin14 is left
encode = [pin15, pin14] 

def countRotations(n, maxRot, speed1):  # n is which wheel, maxRot is the number of rotations to check against, and speed1 is the primary speed
    # similar to the wheel function in the raspi wheelEncoder class.
    if (rotations[n] >= maxRot):  # if the current number of rotations is the amount desired or more, shut off the wheel.
        toggle[n] = 0
        car.set_speed(n, speed1*toggle[n])  # sets the motor n speed to 0
        print("turning wheel " + str(n) + " off")
    rotations[n] = rotations[n] + 5  # every time it's called it increments by 5, which is 1/20th of 100 (1 rotation)

def driveRotations(r=3, maxspeed=-64, minspeed=-16):  # r is the number of rotations, maxspeed is the maximum speed, and minspeed is the minimum
    
    car.enable(True)  # turns on car
    state = [maxspeed, maxspeed]  # sets the state of each wheel (max or min speed) to maxspeed
    speed1 = maxspeed
    speed2 = minspeed
    counter = 0  # counter is used for printing / trouble shooting only
    if r <= 0:  # if rotations is negative, make it positive
        r = r*-1
    rot = r * 100  # rotations turned into 100/rotation since the encoder is in 20ths
    if speed1 > -16:  # if max speed is too low, make it -16
        speed1 = -16
    if speed2 < speed1:  # if minspeed is more negative than maxspeed, make it into 1/4th of maxspeed
        speed2 = 1/4 * speed1
    if speed2 > -8:  # if the minspeed is more than -8 (so -7 onwards) then become -8
        speed2 = -8
    while toggle[1] or toggle[0]:  # as long as one of the wheels isn't toggled off.
        car.drive(state[1] * toggle[1], state[0] * toggle[0])  # at the start of each loop, set the speed to their speed, and multiply by either 0 or 1
        time.sleep(0.001)  # real short delay
        for n in range(0, 2):  # for each wheel/encoder
            In[n] = encode[n].read_digital()  # store the current input
            if In[n] == 0 and last[n] == 1:  # if the current input and the last input are different (if the wheel is moving)
                countRotations(n, rot, speed1)  # count rotations for wheel n for the number of rotations.

            last[n] = In[n]  # last input is the current input. but at the end
        if rotations[1] >= rotations[0]:  # if wheel 1 is faster than wheel 0, set wheel 0 to max speed
            state[0] = speed1
        else:  # otherwise, wheel 0 is ahead of wheel1 and needs to slow down
            state[0] = speed2
        if rotations[0] >= rotations[1]:  # same story for wheel 0 faster than wheel 1
            state[1] = speed1
        else:
            state[1] = speed2
    
    car.enable(False)
    dist = ((rotations[1] + rotations[0]) / 200) * 20.42  # approximate distance traveled
    print("traveled approximately " + str(dist) + " cm")  # print the distance traveled
    __reset_variables()  # clear the variables for next time it's called.
    
#def driveCM(cm, maxspeed, minspeed):  # not currently working
#    dist = cm/20.4
#    print(dist)
#    driveRotations(dist, maxspeed, minspeed)

def __getRotations(n):  # returns the number of rotations for wheel n
    return rotations[n] / 100.0

def __reset_variables():  # resets all of the global variables.
    for n in range(0, 2):
        rotations[n] = 0
        In[n] = 0
        toggle[n] = 1

def cm_to_rotations(cm):  # converts a distance in cm to the right number of rotations
    return cm/20.42  # 20.42 is 204.2mm which is the wheels circumference

while True:  # actual program that runs
    if button_a.was_pressed():  # when a is pressed, drive 2 rotations.
        car.enable(True)
        driveRotations(2, -64, -24)
    elif button_b.was_pressed():  # when b is pressed, drive ~100cm
        car.enable(True)
        driveRotations(cm_to_rotations(100), -64, -24)
    else:  # if nothing was pressed, wait half a second
        time.sleep(0.5) 