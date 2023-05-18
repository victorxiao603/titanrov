import time   
import pigpio
import numpy
import ROV_Controller

CLAW_PIN = 13
CLAW_OPEN = 1890
CLAW_CLOSE = 1110

def Init():
    time.sleep(1)                                                                                                                                                                           

    global pi
    pi = pigpio.pi()
    
    if not pi.connected:
        print("Claw initialization fail")
    
    # Sets the claw to be opened 
    Output(1890)
    global arm_open
    arm_open = [1]
 
def Output(speed):
    pi.set_servo_pulsewidth(CLAW_PIN,speed)

def Open_Close():
    if arm_open[0] == 0: # If the claw is open then close it
        Output(CLAW_OPEN)
        arm_open[0] = 1
    else:                # If the claw is closed then open it
        Output(CLAW_CLOSE)
        arm_open[0] = 0
        
    time.sleep(0.3) # Time to wait for the next input to open or close the claw

def End():
    Output(CLAW_OPEN) # Opens the claw when ending the program
    time.sleep(1)
    pi.stop()