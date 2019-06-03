# Lesson 3, align the robot with the magnetic north
from microbit import *
# motobit "library" will replace with an import if we get it working.
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

if not compass.is_calibrated:
    compass.calibrate()
car = motobit()
while True:
    compassHeading = 34  # set the compass heading to any value between 2 and 70, in this case choosing 34
    while compassHeading > 2 and compassHeading < 70: # not looking north
        compassHeading = compass.heading()/5  # divide 360 into 72 values
        car.enable(True)
        if(compassHeading <= 36):
            car.drive(32, -32)  # turn
        elif (compassHeading > 36):
            car.drive(-32, 32)
    car.enable(False)
