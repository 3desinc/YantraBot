#!/usr/bin/env python3

#from rrb3 import *
#from time import sleep

# Initialize variables
#rr = RRB3(9,6)

# Get initial read of distance from any random obstacle to Robot, assume 10 cm.
#read initial distance
distance = 25

lastdist = distance
avgdist = 0
try:
    while True:
        # Take the average distance, to eliminate outliers
        avgdist = (distance + lastdist)/2 
        if(avgdist > 15):
            # Keep going forward
            print("Going forward...distance more than 15 cm")
            distance = 12
        elif(avgdist > 10):
            # Keep going forward
            print("Still going forward...distance between 10 & 15 cm")
            distance = 8
        else:
            # Go reverse
            print("Else back off...less than 10 cm")
            sleep(1)
            print("take a slight left turn")
        lastdist = distance
        print("Again get current distance")
        distance = 25
        # Print current distance of Obstacle if any
        print(distance)
        # 
        # Stop Robot momentarily - May not be noticable.
        #rr.set_motors(0,0,0,0)
        # Check & Print distance again.
        print(distance)
except KeyboardInterrupt:
    rr.stop()