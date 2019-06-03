#!/usr/bin/env python3

## This is an example program showing how to use the two LED's on the rrb3 raspi hat
## written by Martin Dickie
## last edited by Martin Dickie 7/20/18

from rrb3 import * #import all of rrb3
from timer import sleep #imports the sleep command from timer, because we're not doing anything else with timer we can ask to only have sleep.

rr = RRB3(9,6) # set up the RRB board controls as rr, and the robot has 9 volts with motors asking for 6.

try: # will do this until the exception

    while(True): # does a loop forever that turns on one LED and turns off the other, every second.
    
        rr.set_led1(1) # this talks to the board (rr) and tells it to set led1 to 1 (on)
    
        rr.set_led2(0) # this one tells the board (rr) to set led2 to 0 (off)
    
        sleep(1) # the program will wait 1 second before continuing
    
        rr.set_led1(0) # this time the board is told to set led1 to 0 (off)
    
        rr.set_led2(1) # and led2 to 1 (on), essentially blinking the lights every second.

except KeyboardInterrupt: # if you press ctrl + C at the same time, it makes a "keyboard interrupt" which stops the program.
                          # in this case the program then makes sure to do some things before it stops completely
    rr.set_led1(0) # it turns off both of the led's

    rr.set_led2(0)

    rr.stop() # and tells the board (rr) to stop, which resets all of its settings.
