# Lesson 9 - controller
# in this lesson there will be 2 parts, one part for the robot
# and one part for a remote controller (this one)
from microbit import *
import radio
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
radio.on()
toggle = True
while True:
    while toggle:
        if accelerometer.was_gesture('shake'):
            radio.send('STOP')
            display.show(Image.SKULL)
        elif accelerometer.was_gesture('left'):
            radio.send('LEFT')
            display.show(Image.ARROW_W)
        elif accelerometer.was_gesture('right'):
            radio.send('RIGHT')
            display.show(Image.ARROW_E)
        elif accelerometer.was_gesture('down'):
            radio.send('FORWARD')
            display.show(Image.ARROW_N)
        elif accelerometer.was_gesture('up'):
            radio.send('BACKWARD')
            display.show(Image.ARROW_S)
        if button_b.was_pressed():
            toggle = False
    if button_a.was_pressed():
        toggle = True
    time.sleep(0.01)