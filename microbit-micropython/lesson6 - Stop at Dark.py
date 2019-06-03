# Lesson 6, stop at dark
# the microbit uses a photoresistor (light sensor) and when it reaches 0 brightness it stops
# at 1 brightness it backs up, and 2/3 it drives forward
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
# just a fancy image of a fully filled square.
fullSquare = Image("88888:""85558:""85958:""85558:""88888:")
toggle = True  # toggle for motors, this way things that turn off the motor
# don't mess with the buttons
while True:
    # setup for brightness reading, for whatever reason doing lots of steps
    # at once was being weird.
    brightness = 1023  # inverting the light, so starting at 1023 and the subtracting the reading of brightness
    brightness = brightness - pin1.read_analog()  
    sizedBrightness = int(brightness / 256)  # split the brightness reading into 4 parts 0,1,2,3
    car.enable(toggle)
    if sizedBrightness == 0:  # if it's too dark, the car stops.
        display.clear()
        car.enable(False)
        time.sleep(0.1)
    elif sizedBrightness == 1:  # if it's pretty dark the car backs up
        display.show(Image("00000:""00000:""00900:""00000:""00000:"))
        car.drive(64, 64)
        time.sleep(0.1)
    elif sizedBrightness == 2:  # if it's normal lighting it drives forwards
        display.show(Image.SQUARE_SMALL)
        car.drive(-54, -54)
        time.sleep(0.1)
    elif sizedBrightness == 3:  # likewise for when it's bright, just faster
        display.show(fullSquare)
        car.drive(-64, -64)
        time.sleep(0.1)
    if button_a.was_pressed():
        toggle = True
    if button_b.was_pressed():
        toggle = False
