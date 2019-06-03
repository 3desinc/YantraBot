from rrb3 import *
from time import sleep

rr = RRB3(9,6)

while True:
    user = (input("input direction"))
    if(user == 'w'):
        rr.forward(0.5)
    elif(user == 'a'):
        rr.left(.55)
    elif(user == 'd'):
        rr.right(.55)
    elif(user == 's'):
        rr.reverse(0.5)
    
