#!/usr/bin/env python3

from rrb3 import *

rr = RRB3(9,6)
try:
    while True:
        rr.forward(1,.8)
        rr.right(1)
except KeyboardInterrupt:
    rr.stop()
    

	
