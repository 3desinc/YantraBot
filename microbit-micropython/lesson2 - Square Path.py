# Lesson 2, Follow the path of a square
from microbit import *
import time
# motobit class, cannot import
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

car = motobit()

while True:  # while looping, check buttons being pressed
    if button_a.was_pressed():  # when a is pressed, do things
        try:  # try to do these things, and then when b is pressed it interrupts
            for a in range(0, 4):  # repeat 4 times
                car.enable(True)  # turn on car
                car.drive(-64, -64)  # drive straight at half speed.
                # for loop is to make the button being pressed more precise, now it checks every half second vs
                # the normal 2 seconds it would run before checking for the button being pressed.
                for i in range(0, 4):
                    time.sleep(0.5)
                    if button_b.was_pressed():
                        # The value error is just an error to be caught by the except to stop the car.
                        raise ValueError("button b is pressed")
                car.drive(50, -45)
                time.sleep(0.5)
                if button_b.was_pressed():
                    raise ValueError
                car.enable(False)
        except ValueError:  # when b is pressed, stop the car.
            car.enable(False)
