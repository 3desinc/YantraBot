# lesson - ? Ultrasonic sensor
# will drive forward, and when detects an object close (by using the ultrasonic sensor) it will backup and turn
from microbit import *
import time
import machine
# motobit class, would be imported but having some issues.
class motobit:
    moto_l = 0x21
    moto_r = 0x20
    moto_on = 0x70
    
    def __init__(self, address=0x59):
        self.ADDR = address
        i2c.init()  
          
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
# Ultrasonic class, used for getting distance
class ultrasonic:
    
    def __init__(self):
        global echo
        echo = pin8  # echo pin is pin8
        global trig
        trig = pin12  # trig pin is pin12

    def _send_trigger_pulse(self):
        trig.write_digital(1)
        time.sleep(0.0001)
        trig.write_digital(0)

    def _wait_for_echo(self, value, timeout):
        count = timeout
        while echo.read_digital() != value and count > 0:
            count -= 1

    def get_distance(self):
        self._send_trigger_pulse()
        self._wait_for_echo(True, 10000)
        start = time.ticks_us()
        self._wait_for_echo(False, 10000)
        finish = time.ticks_us()
        pulse_len = finish - start
        distance_cm = pulse_len / 29 / 2
        return distance_cm
        
car = motobit()
toggle = True
us = ultrasonic()
while True:
    car.enable(toggle)
    if toggle:
        dist = us.get_distance()
        print(dist)

    if dist > 30:
        car.drive(-64, -64)
        time.sleep(0.1)
    elif dist > 10:
        car.drive(-32 - int(dist), -32 - int(dist))
        time.sleep(0.1)
    elif dist <= 10:
        car.drive(64, 64)
        time.sleep(0.6)
        car.drive(64, -64)
        time.sleep(0.25)
        car.drive(48, 48)
    if button_a.was_pressed():
        toggle = True
    if button_b.was_pressed():
        toggle = False
    