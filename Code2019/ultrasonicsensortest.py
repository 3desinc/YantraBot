#!/usr/bin/env python3

from rrb3 import *
from time import sleep

# Initialize variables
rr = RRB3(9,6)

# Get initial read of distance from any random obstacle to Robot
distance = rr.get_distance() 
lastdist = distance
avgdist = 0
try:
    while True:
        # Take the average distance, to eliminate outliers
        avgdist = (distance + lastdist)/2 
        if(avgdist > 10):
            # Keep going forward
            rr.set_motors(0.3,0,0.3,0)
        elif(avgdist > 15):
            # Keep going forward
            rr.set_motors(0.6,0,0.6,0)
        else:
            # Go reverse
            rr.set_motors(0.5,1,0.5,1)
            sleep(1)
            rr.left(0.5)
        lastdist = distance
        distance = rr.get_distance()
## distance is in "cm" & a float number. So need to print in "int"
        print(int(distance))
##   =======
        # Stop Robot momentarily - May not be noticable.
        #rr.set_motors(0,0,0,0)
        #print(int(distance))
## Takes care of any exception & cleanup() resets the GPIO pins
except:
    rr.stop()
    rr.cleanup()