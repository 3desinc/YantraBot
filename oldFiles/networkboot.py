#!/usr/bin/env python3
#networkboot.py this is a script that will configure the nextwork configurations for our raspberry pi's
#to automatically connect to a router and assign a static ip address.
#@author Martin Dickie
#Notice, this script only works for linux systems
#This script also requires for the user to have the Yantrabot git libray in their user directory /home/username
from shutil import copyfile
import getpass
import os
username = "martin" # change to whatever your username is
iteratorFile = open("/home/"+username+"/Yantrabot/iterator.txt","r") # open the iterator file, read the value and store it
iterator = int(iteratorFile.readline())
iteratorFile.close() 
routerip = "192.168.0.1" # router ip
static_ip = "192.168.0." + str(iterator+120) #assigned static ip
try:
        hostname = open("/media/"+username+"/rootfs/etc/hostname","w+")
        hostname.write("Raspi-"+str(iterator)) # host name is raspi-number
        print("hostname successful")
        hostname.close()
except:
        print("hostname failed")
try:
        file2 = open("/media/"+username+"/rootfs/etc/dhcpcd.conf","w")
        file2.write("# here is an example which configures a static address, routes and dns.\ninterface eth0\nstatic ip_address=10.1.1.30/24\nstatic routers=10.1.1.1\nstatic domain_name_servers=10.1.1.1\n\ninterface wlan0\nstatic ip_address="+static_ip+"/24\nstatic routers="+routerip+"\nstatic domain_name_servers="+routerip)
        print("dhcpcd.conf successful")
        file2.close()
except:
        print("dhcpcd.conf failed")
try:
        copyfile("/home/"+username+"/Yantrabot/network/wpa_supplicant.conf","/media/"+username+"/rootfs/etc/wpa_supplicant/wpa_supplicant.conf")
        print("wpa_supplicant.conf copied successfuly")
except:
        print("failed to copy wpa_supplicant.conf, try updating directory paths")
try:
        interface = open("/media/"+username+"/rootfs/etc/network/interfaces","w")
        interface.write("# interfaces(5) file used by ifup(8) and ifdown(8)\n\n# Please note that this file is written to be used with dhcpcd\n# For static IP, consult /etc/dhcpcd.conf and 'man dgcocd.conf'\n\n# Include files from /etc/network/interfaces.d:\nsource-directory /etc/network/interfaces.d")
        interface.close()
        print("interface file successful")
except:
        print("interface file failed")
#reopen the iterator file, and increase the iterator by one.
try:
        iteratorFile = open("/home/martin/Yantrabot/iterator.txt","w")
        iteratorFile.write(str(iterator+1))
        iteratorFile.close()
        print("iterator increased")
except:
        print("iterator failed to increase")
       
