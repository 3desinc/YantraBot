#!/usr/bin/env python3

#from rrb3 import *
#from time import sleep

# RRB3(a,b) a is voltage for batteries,
# b is voltage for motors
#rr = RRB3(9,6)

## try right for 0.63 seconds, which is aproximately 90 degrees
#rr.right(0.63) 

# What does while True: do?
# Use the for loop to do 4 sides of the square.
try:
    for i in range(1,5):
        print(i)
        # Go forward number of Seconds & Speed
        #rr.forward(5, 0.8)
        #rr.right(5, 0.3)
except KeyboardInterrupt:
        rr.stop()
    
    
    
    
 