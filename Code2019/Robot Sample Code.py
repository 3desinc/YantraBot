#!/usr/bin/env python3
# Name: Satish Mantripragada
# Course: Introduction to 3D Modeling & Robotics
# Program Name: Set LEDs

from rrb3 import *
from time import sleep
rr = RRB3(9,6)
try:
    while True:
        rr.set_led1(1)
    # Every 1000 ms (1 sec)
        sleep(2)
        rr.set_led2(1)
        sleep(2)
        rr.set_led1(0)
        rr.set_led2(0)
        sleep(2)
except keyboardInterrupt:
        rr.set_led1(0)
        rr.set_led2(0)
except:
        rr.set_led1(0)
        rr.set_led2(0)