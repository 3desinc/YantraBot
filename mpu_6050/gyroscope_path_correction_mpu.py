#!/usr/bin/env python
# uses the gyroscope to read when drifting (mostly) and correct the path to go straight
from rrb3 import *
import time
import read_mpu_6050 as reader

rr = RRB3(9,4.5) # the 4.5v is for the motors, slowing it down.
last = [0,0,0,0,0] # array of last 5 values read
avgGyro = 0


try: # setup
    for n in range(0,5) # iterate 5 times to get 5 values for the gyroscope to start
        last[n] = reader.get_gyro_z
    while True: # program, will end when CTRL + C is pressed 
        current = reader.get_gyro_z() # read gyroscope value
        print("newest value: " + str(current)) # print newest value
        avgGyro = 0 # reset average value, so that it can be recalculated
        for lastIterator in range(1,5): # iterate through the last values (increasing by 1 each time it loops)
            last[lastIterator] = last[lastIterator-1] 
            avgGyro = avgGyro + last[lastIterator] # add values to get average
        avgGyro = avgGyro/5 # calculate average, 5 is the number of iterations in the loop
        if avgGyro > 0: # print positive numbers for filtering purposes
            print("positive average: " + str(avgGyro))
        elif avgGyro < 0: # print negative numbers for filtering purposes
            print("negative average: " + str(avgGyro))
        else: # print zeros for filtering
            print("zero " + str(avgGyro))
        if avgGyro not == 0 # if it's not reading zero (if the sensor wasn't reading for example it'd be zero)
            if abs(avgGyro) - abs(current) < -10: # if the newest value is larger than the average value, 
                                                  # -10 is because the average reading is positive and usually spikes in that direction.
                print("rotating left from: " +str(abs(avgGyro) - abs(current)) + " or " + str(current))
                rr.set_motors(0.4,0,0.5,0) # slow down the left motor, so turn left
                time.sleep(0.1) # correcting for 0.1 seconds.
            
            if abs(avgGyro) - abs(current) > -1.5: # -1.5 is from testing, the average reading is around 5, so when it dips to 3.5 or lower then it's moving left, and needs corrected 
                print("rotating right from negative: " + str(abs(avgGyro) - abs(current)) + " or " + str(current))
                rr.set_motors(0.5,0,0.4,0) # slow down right motor, so turn right
                time.sleep(0.2) # corrects for 0.2 seconds, this is because the wheels are slightly different power levels
                
        rr.set_motors(0.5,0,0.5,0) # set the motors back to normal
        time.sleep(0.1)  # drive for 0.1 seconds before rescanning ( value is arbitrary, encoders would help with knowing what value to use )
        last[0] = current # set the last value to the current value
except KeyboardInterrupt:
    print("stopping")
    rr.stop()
