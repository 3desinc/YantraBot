#!/usr/bin/env python3
#networkboot.py this is a script that will configure the nextwork configurations for our raspberry pi's to automatically connect to a router and assign a static ip address.
#@author Martin Dickie
#Notice, this script only works for linux systems
#This script also requires for the user to have the Yantrabot git libray
#Last edited by Martin Dickie 7/20/18
from shutil import copyfile
import getpass
import os
username = "martin" # change to whatever your username is on your computer
route_to_Yantrabot = "/home/"+username+"/Yantrabot" #shorthand path to Yantrabot
iteratorFile = open(route_to_Yantrabot+"/iterator.txt","r") # open the iterator file, read the value and store it
iterator = int(iteratorFile.readline())
print("card \# "+str(iterator))
iteratorFile.close() 

route_to_sd_etc = "/media/"+username+"/rootfs/etc/" # the directory of etc, used a couple times here
routerip = "192.168.1.1" # the router IP
wpa_supplicant = "nscc_wpa_supplicant.conf" # the name of the wpa_supplicant file to be duplicated
baseIP = 120 # starting number for the static ip
static_ip = "192.168.1."+ str(iterator+baseIP) # assigned static ip for second connection
try: # open the hostname file, and change it to be "Raspi-#" # being the iterator number
        hostname = open(route_to_sd_etc+"hostname","w+")
        hostname.write("Raspi-"+str(iterator)) # host name is raspi-number
        print("hostname successful") # confirms that the hostname file has been found and changed
        hostname.close() # closes the file
except: # if it fails to open the hostname file, it will print that it failed
        print("hostname failed") 
try: # opens the dhcpcd.conf and re-writes it to have the correct static ip, router ip etc..
        file2 = open(route_to_sd_etc+"dhcpcd.conf","w")
        file2.write("# here is an example which configures a static address, routes and dns.\ninterface eth0\nstatic ip_address=10.1.1.30/24\nstatic routers=10.1.1.1\nstatic domain_name_servers=10.1.1.1\n\ninterface wlan0\n\nstatic ip_address="+static_ip+"/24\nstatic routers="+routerip+"\nstatic domain_name_servers="+routerip)
        print("dhcpcd.conf successful")
        file2.close()
except: # if it fails to open dhcpcd.conf then it will say it failed
        print("dhcpcd.conf failed")
try: # copies the wpa_supplicant file provided into the wpa_supplicant.conf on the pi
        copyfile(route_to_Yantrabot+"/network/"+wpa_supplicant,route_to_sd_etc+"wpa_supplicant/wpa_supplicant.conf")
        print("wpa_supplicant.conf copied successfuly")
except: # if it fails to find the wpa_supplicant, then error
        print("failed to copy wpa_supplicant.conf, try updating directory paths")
try: # re-writes the interfaces file to not interfere with anything
        interface = open(route_to_sd_etc+"/network/interfaces","w")
        interface.write("auto wlan0\n# interfaces(5) file used by ifup(8) and ifdown(8)\n\n# Please note that this file is written to be used with dhcpcd\n# For static IP, consult /etc/dhcpcd.conf and 'man dgcocd.conf'\n\n# Include files from /etc/network/interfaces.d:\nsource-directory /etc/network/interfaces.d\nallow-hotplug wlan0\niface wlan0 inet dhcp\nwpa-conf /etc/wpa_supplicant/wpa_supplicant.conf\niface default inet dhcp")
        interface.close()
        print("interface file successful")
except: # if it fails to find the interface file it will say so
        print("interface file failed")
#reopen the iterator file, and increase the iterator by one.
try:
        iteratorFile = open(route_to_Yantrabot+"/iterator.txt","w")
        iteratorFile.write(str(iterator+1))
        iteratorFile.close()
        print("iterator increased")
except:
        print("iterator failed to increase")
