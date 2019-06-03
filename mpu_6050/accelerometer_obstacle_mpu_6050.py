#!/usr/bin/env python
# This reads accelerometer, uses the data to detects bump/collision of the Robot
# Estimates how far it is goes for the duration so the program. - estimated travel distance:
# Estimates how fast the Robot is travelling - Average acceleration
import read_mpu_6050 as reader
from rrb3 import *
import time
import random

rr = RRB3(9,6)
last = [0,0,0,0,0]
goingForward = True
goingBackward = False
status = 0
totTime = 0
travelTime = 0
avgAcc = 0
velocity = 0
starttime = time.time()
try: # setup for loop
    for speedup in range(0,55,5): # increase the speed of the robot at 0.05 per iteration
        speed = speedup/100 # convert iterations of the loop into a partial value for the speed
        start = time.time() # keeps track of time accelerating
        rr.set_motors(speed,0,speed,0)
        afterAcc = reader.get_x_Acc() # read acceleration immediately after increasing speed
        finish = time.time() # keeps track of time accelerating
        totTime = (finish - start) + totTime # calculate total time accelerating
        avgAcc = (afterAcc) + avgAcc # add all accelerations and add to average after
    avgAcc = avgAcc/11 # divide by the total iterations to get average
    avgAcc = avgAcc * 9.81 # multiply by 9.81 to convert from g to m/s (g is 9.81m/s)
    velocity = avgAcc*totTime
    # print the values of average acceleration, the time it took to accelerate and the estimated speed. 
    print("average acceleration: " + str(avgAcc) + " total time " + str(totTime) + " velocity: " + str(velocity))
    starttime = time.time() # reset timer to ignore 'calibration'
    
    # loop which is main program, will end when CTRL+C is pressed.
    while True:
        timeTicker = time.time() # keep track of time traveling
        lastAvg = 0
        for a in range(1,5): # cycle through the last 5 inputs
            last[a] = last[a-1]
            lastAvg = last[a] + lastAvg
        lastAvg = lastAvg/5  # get average last value
        current = reader.get_x_Acc()  # read acceleration value
        print(current - lastAvg) # print the compared number
        # if it detects a sudden change in acceleration (hitting a barrier for example)
        if (current - lastAvg > 0.4 or current - lastAvg < -0.4) and correcting == False:
            print("detected " + str(current - lastAvg)) # print the value that it read when it hit a value
            rr.set_motors(0.4,1,0.4,1) # backs up for 1 second
            time.sleep(1) 
            rr.set_motors(0.5,1,0.5,0) # and then turns left for 0.3 seconds
            time.sleep(0.3)
            rr.set_motors(0.5,0,0.5,0) # set motors to forward
            correcting = True # don't keep track of time traveling if it hit a barrier and turns
        else:
            rr.set_motors(0.5,0,0.5,0)
            correcting = False # marks that it traveled this loop
        last[0] = current # update last value with the current one
        if correcting == False: # if it didn't hit an object then add time to the time traveled
            travelTime = travelTime + (time.time()-timeTicker)
except KeyboardInterrupt: # when the program stops (you pressing CTRL + C)
    print("stopping")
    finishtime = time.time() - starttime # time the program ran for
    print("total duration: " + str(finishtime)+ "s") # prints time it ran for
    print("duration driving forward: " + str(travelTime)) # prints how long it was traveling forward
    print("estimated travel distance: " + str(avgAcc*totTime*travelTime)) # prints the estimated distance traveled
    rr.stop()
