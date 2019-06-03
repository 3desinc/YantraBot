#!/usr/bin/env python3
# Written by Martin Dickie for 3DESinc
# last modified 7/23/18
# This is an example program for running the motors. This requires the raspirobotboard3 library and hat for the Raspberry pi.

from rrb3 import * # import everything from rrb3, which is the raspirobotboard3
from time import sleep # import the sleep function from time
voltage = 9 # the voltage of the batteries (9v)
motorvolt = 6 # the voltage the motors will need (6v)

duration = 1 # how long to run each command for
speed = 0.5 # how fast to make the robot, 1 = 100% so 0.5 = 50% speed

rr = RRB3(voltage,motorvolt) # setup the RRB3 to account for voltage of motors and batteries. using rr as the variable for the rest of the program.

try: # try to run program, if there's failure or an exception it will stop.
        while True: # while True is infinite
                rr.forward(duration,speed) # move forward for duration seconds, at speed speed.
                rr.reverse(duration,speed) # move backwards for duration seconds, at speed speed.
                rr.right(duration,speed) # rotate right for duration seconds, at speed speed.
                rr.left(duration,speed) # rotate left for duration seconds, at speed speed.
                #loop infinitely
except KeyboardInterrupt: # Ctrl+C in command prompt will stop the program, if we didn't cleanup the exception then the engines would go forever. 
        rr.cleanup() # cleans up all of the rrb things plus everything GPIO does as cleanup as well.


