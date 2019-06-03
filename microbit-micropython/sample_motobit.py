import time
import motobit
from microbit import *
a = 0
while True:
    time.sleep(1)
    car = motobit.motobit()
    if button_b.is_pressed() and button_a.is_pressed():
        display.show(Image.ARROW_N)
        car.enable(False)
    elif button_b.is_pressed():
        display.show(Image.HAPPY)
        a = -1
        car.enable(True)
    elif button_a.is_pressed():
        display.show(Image.SAD)
        car.enable(True)
        a = 1
    else:
        display.clear()
    car.drive(a*-64, a*-64)