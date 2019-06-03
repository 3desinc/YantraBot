from rrb3 import *
from time import sleep
rr = RRB3(9,6)
## RRB3(a,b) a is voltage for batteries,
##b is voltage for motors

speed = .9
rr.forward(speed)
while(speed > 0):
    rr.set_motors(speed,0,speed,0)
    sleep(0.2)
    speed = speed - 0.05
rr.stop()

