import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program

Hz = 0
bright_level = 0

def Init():
    global led1
    print("Initializing LED")   
    IO.setwarnings(False)           #do not show any warnings
    IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
    IO.setup(3,IO.OUT)           # initialize GPIO19 as an output.
    led1 = IO.PWM(3,50)          #GPIO19 as PWM output, with 100Hz frequency
    led1.start(0)                              #generate PWM signal with 0% duty cycle 


def change_brightness():
    global led1
    global Hz
    global bright_level
    if bright_level == 0:
        Hz = 0
    elif bright_level == 1:
        Hz = 60
    elif bright_level == 2:
        Hz = 100
    else: Hz = 0
    
    led1.ChangeDutyCycle(Hz)
    
    bright_level = bright_level + 1
    bright_level = bright_level % 3



