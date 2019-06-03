# Lesson 9 - robot, Control the robot remotely
# in this lesson there will be 2 parts, one part for the robot (this one)
# and one part for a remote controller
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
radio.on()  # turn radio on
toggle = True  # set toggle of motors to on
while True:
    car.enable(toggle)
    incoming = radio.receive()  # read incoming radio
    if incoming == 'STOP':  # if it sends stop, stop
        toggle = False
    elif incoming == 'FORWARD':  # if it sends forward, drive for .2 sec
        car.drive(-32, -32)
        display.show(Image.ARROW_N)
    elif incoming == 'BACKWARD':
        car.drive(32, 32)
        display.show(Image.ARROW_S)
    elif incoming == 'RIGHT':
        car.drive(-32, 32)
        display.show(Image.ARROW_E)
    elif incoming == 'LEFT':
        car.drive(32, -32)
        display.show(Image.ARROW_W)
    time.sleep(0.2)  # drive for 0.2 seconds and then turn off.
    car.drive(0, 0)
    if button_a.was_pressed():
        toggle = True
    if button_b.was_pressed():
        toggle = False