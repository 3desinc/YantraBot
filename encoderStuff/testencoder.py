import sys
sys.path.append('/home/pi/Yantrabot/encoderStuff/')
import WheelEncoder as we
try:
    try:
        dist = sys.argv[1]
        dist = float(dist)
    except:
        dist = 10
    try:
        max = sys.argv[2]
        max = float(max)
    except:
        max = 0.4
    try:
        min = sys.argv[3]
        min = float(min)
    except:
        min = 0.1
    we.driveCM(dist,max,min)
except KeyboardInterrupt:
    we.stop()
except:
    we.stop()
