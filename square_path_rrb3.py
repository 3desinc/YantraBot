#!/usr/bin/env python3

from rrb3 import *
from time import sleep
rr = RRB3(9,6)
## RRB3(a,b) a is voltage for batteries,
##b is voltage for motors

## try to run the program, so that it can catch keyboard interrupts and
## properly shutdown the board.
try:
    while(True):
        ## Moves forward for 3 seconds at half speed 
        rr.forward(3,0.5)
        ## turns right for 0.63 seconds, which is aproximately 90 degrees
        rr.right(0.63)
except KeyboardInterrupt:
    rr.stop()
    
