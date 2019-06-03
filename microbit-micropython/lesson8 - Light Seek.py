# Lesson 8, follow the bright light
# the robot has 2 photo resistors on it, follow the brighter one
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
        
car = motobit()
toggle = True
while True:
    left_light = int(pin0.read_analog())
    right_light = int(pin1.read_analog())
    left_light = (1023 - left_light) / 64  # turn into 16ths
    right_light = (1023 - right_light) / 64  # to keep values easier to compare

    car.enable(toggle)
    if abs(left_light - right_light) == 0:  # if fully dark, backup and show skull
        display.show(Image.SKULL)
        car.drive(-64, -64)
        time.sleep(0.1)
    
    elif left_light > right_light + 1:  # if left is more than right(plus variance)
        display.show(Image.ARROW_W)
        car.drive(32, -32)
        time.sleep(0.3)
        
    elif right_light > left_light:  # if right is more than left, was a weaker sensor so don't need the +
        display.show(Image.ARROW_E)
        car.drive(-32, 32)
        time.sleep(0.3)
    
    else:  # default drive forward
        display.show(Image.ARROW_N)
        car.drive(-64, -64)
        time.sleep(0.1)
        
    if button_a.was_pressed():
        toggle = True
    if button_b.was_pressed():
        toggle = False
