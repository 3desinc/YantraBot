#!/usr/bin/env python
# Creat function readAcc(), get_x_Acc() & others
#Process_mpu_6050, gyroscope_mpu programs call these functions
#
import mpu_6050 as mpu
import time
pollTimes = 15
try:
    mpu.initmpu()
except IOError:
    print(IOError)
    
# outputs the accelerometer data into tempAccData.txt
# returns average accelerometer value from 15 readings
def readAcc():
    totAcc_x = 0
    totAcc_y = 0
    totAcc_z = 0
    try:
        tempAccData = open("tempAccData.txt","w")
        for a in range(0,pollTimes):
            mpu.get_data()
            totAcc_x = totAcc_x + mpu.acc_x
            totAcc_y = totAcc_y + mpu.acc_y
            totAcc_z = totAcc_z + mpu.acc_z
            tempAccData.write(str(mpu.acc_x) + " " + str(mpu.acc_y) + " " + str(mpu.acc_z) + "\n")
        avgAcc_x = totAcc_x / pollTimes
        avgAcc_y = totAcc_y / pollTimes
        avgAcc_z = totAcc_z / pollTimes
        avgAcc = str(avgAcc_x) + " " + str(avgAcc_y) + " " + str(avgAcc_z)
        tempAccData.write("Averages:\n" + avgAcc)
        tempAccData.close()
        return avgAcc
    except IOError:
        print(IOError)
# gets accelerometer x value
def get_x_Acc():
    mpu.get_data()
    return mpu.acc_x
# gets accelerometer y value
def get_y_Acc():
    mpu.get_data()
    return mpu.acc_y
# gets accelerometer z value
def get_z_Acc():
    mpu.get_data()
    return mpu.acc_z
# reads from tempAccData and returns the average value (stored at the bottom of the file)
def access_x_acc():
    tad = open("tempAccData.txt","r")
    for a in range(0,pollTimes+2):
        print(a)
        x = tad.readline()
        print(x)
    tad.close()
    return float(x[0:x.find(" ")])
# gets the gyroscope z value (left and right on the raspberry pi in current mounting position)
def get_gyro_z():
    mpu.get_data()
    return mpu.gyro_z
