## this is an example of how to write a python file in the right order.
## the reason to do all of the #'s is that it is the way to write comments in python, so the program will ignore everything in a line after the #
## the start of a program if you'd like to run it on the computer without having to specify to run it with python or python3 is by starting the code with the following line. Keep in mind, that it should be at the top of the program above all of these comments, this is just for the example program.
#!/usr/bin/env python3
## what that does is tell the computer that when running this program use python3, which is located in the directory of /usr/bin/env in this case.
## after that you're going to want to import any number of packages which aren't automatically loaded. Some of these may come pre-installed and other ones may need to be downloaded.
## in this class all the packages you will need should be already installed on the pi.

import RPi.GPIO as GPIO # This is importing the GPIO package, which is for raspberry pi to use the pins on it. The "as GPIO" is letting you call it GPIO instead of always saying RPi.GPIO.

from time import sleep ## this is how to import only one command from a package, in this case we only want sleep from time, because no other time command is important in this program.

# After you're done importing all of the things you need for your program, the next thing is to set any variables that you will use for the program.
# The importance of using variables, is that it makes it easier to change things later, as well as make it so that you know what is happening in the code.
# For example, if I were to say GPIO.setup(5,GPIO.IN) then that'd mean to set pin 5 as input, but what is pin 5? If I did GPIO.setup(light_sensor_pin,GPIO.IN) then you know it's for the light sensor.
# to do that, you do the variable name followed by = and then whatever value you'd like it to reference. In this case light_sensor_pin = 5. But you can do much more complicated variables.

led_pin = 7 # here we're saying that whenever you type led_pin it is equivalant to typing 7, that seems like more work for the same thing, but if you wanted to change what pin number to use, then it'd be much easier to set it here than find every time it's used and change those.

# after you setup all of the variables that you're using in your program (you can go back and make more variables later, just put them at the top.) you want to initialize everything.

GPIO.setmode(GPIO.BCM) # this tells the GPIO (raspberry pi controller) to map the pins to the standard of BCM

GPIO.setup(led_pin,GPIO.OUT) # set the led_pin to be an output.

# after initializing everything that you want, then you can start setting up the actual program, first you'll want to setup any functions that will be used in the program. A function is a set of commands that are all put together and so whenever you use the function it does everything inside of it. This is useful for making the program easy to follow, and will save you from having to type a lot of extra code.

def blink_led(duration): # for a function you define the name of it, and then put any parameters that it will have. Here it wants a duration, so we create a variable called duration. Then you do a colon to show that the next things will be part of it.
# the important part about python is that white space matters, so everything indented will relate to the last colon, and then when there's no indent it goes back to the main program.

        GPIO.output(led_pin,True) # this sets the output to be true on the led_pin, which in this case is pin 7. Output being true is basically "on"
        sleep(duration) # the program will sleep for a number of seconds equal to the duration told to the blink_led when it is called.
        GPIO.output(led_pin,False) # this sets the output to be false for led_pin. Which is equivalant of turning the led off.

# now it's time for the actual code that does stuff, everything above is basically setup. Now we'll make an elegant program to blink the led at different speeds, and loop.

# Because we're using a loop that will go forever, it is good to setup a try except, so the program will try to do one thing, and then if it fails the except will do that. Either for a specific exception or all exceptions.

try: # this is where the program is trying to do something
        while True: # while True is an infinite loop, because while will continue until it is false which in this case is never.
                blink_led(0.5) # this will have the led turn on for 500ms, then turn off.
                blink_led(0.75) # turns on the led for 750ms, then off.
                blink_led(1) # turns on the led for 1 second, then off.
                blink_led(2) # turns on the led for 2 seconds, then off.
                # this program will then restart and keep doing it forever... which is until you either close the program, tell it to stop, or press Ctrl + C if in command prompt.
except KeyboardInterrupt: # if the program encounters a keyboard interrupt, (Ctrl + C in command prompt) it will stop the try, and move to except it. In this case it tells the program to cleanup and stop
        GPIO.cleanup() # cleans up the GPIO so that it is back to default, without the led_pin being set as output.
