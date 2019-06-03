# Lesson 7, Avoid Obstacles
# not completed due to sensor being inconsistant
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
    if button_b.was_pressed():
        toggle = False
        
    if button_a.was_pressed():
        toggle = True
    car.enable(toggle)
    detected = 1  # 1 for nothing 0 for detected
    while detected == 1:
        detected = pin8.read_digital()
        if detected == 1:
            car.drive(-16, -16)
            time.sleep(0.5)
        
        if detected == 0:
            car.drive(-25, 25)
            display.show(detected)
            time.sleep(0.5)
            car.enable(False)
            detected = 1
        else:
            display.show(detected)
