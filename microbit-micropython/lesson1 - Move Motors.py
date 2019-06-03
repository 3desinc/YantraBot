# lesson 1, robot basic movements
from microbit import *
import time
# motobit class
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
count = 0
while True:  # always look to see if a button is pressed.
    count = count + 1
    time.sleep(0.1)
    if count %10 == 0:
        print(i2c.scan())
    if button_a.was_pressed():  # when a was pressed, drive forward, turn, drive backward
        car.enable(True)
        car.drive(-64, -64)
        time.sleep(1)
        car.drive(-32, 32)
        time.sleep(1)
        car.drive(64, 64)
        time.sleep(1)
    if button_b.was_pressed():  # when b is pressed, stop the car after 1 second.
        time.sleep(1)
        car.enable(False)
