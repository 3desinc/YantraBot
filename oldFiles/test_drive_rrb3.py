from rrb3 import *
from time import sleep

rr = RRB3(9,6)
try:
    while True:
        rr.set_motors(0.5,0,0.5,0)
        sleep(1)
        rr.set_motors(0.2,0,0.2,0)
        sleep(1)
        rr.set_motors(0.5,1,0.5,1)
        sleep(1)
        rr.set_motors(0.2,1,0.2,1)
        sleep(1)


except KeyboardInterrupt:
    rr.stop()