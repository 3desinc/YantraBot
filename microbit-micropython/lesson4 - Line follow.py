# Lesson 4, line following robot
from microbit import *
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

while True:
    if pin0.read_analog() > 950:  # when reading dark (the line) drive one way
        display.show(Image.ARROW_N)
        car.drive(-45, -22)
    else:  # when reading light, drive the other way.
        display.show(Image.SAD)
        car.drive(-22, -45)
        
    if button_a.was_pressed():
        car.enable(True)
    if button_b.was_pressed():
        car.enable(False)
