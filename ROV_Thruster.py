import time   
import pigpio
import numpy

# ESC_BL = 17  #Connect the ESC in this GPIO pin, right thruster
# ESC_BR = 5 #Connect the ESC in this GPIO pin, front thruster 
# ESC_L = 25 #Connect the ESC in this GPIO pin, back thruster 
# ESC_R = 27 #Connect the ESC in this GPIO pin, left thruster  
# ESC_FR = 16 # 
# ESC_FL = 26 # 

ESC_L = 16  #Connect the ESC in this GPIO pin, right thruster 3
ESC_R = 5 #Connect the ESC in this GPIO pin, front thruster 6
ESC_BL = 25 #Connect the ESC in this GPIO pin, back thruster 2
ESC_BR = 17 #Connect the ESC in this GPIO pin, left thruster  5
ESC_FR = 27 # 4                        
ESC_FL = 26 # 1                                     

def Init():
    time.sleep(1)                                                                                                                                                                           
    global pin_array
    pin_array = [ESC_FL,ESC_BL,ESC_L,ESC_FR,ESC_BR,ESC_R]
    
    global pi
    pi = pigpio.pi()

    if not pi.connected:
        print("Motor initialization failure")
        
    global inputs
    inputs = [1500,1500,1500,1500,1500,1500] #[F_L,B_L,L,F_R,B_R,R]
    
def Calibrate():
    max_value = 2000 #ESC max input value
    min_value = 1500  #ESC min input value

    #Calibrate ESC everytime after powering on  
    Output_All(max_value)
    time.sleep(3)
 
    Output_All(min_value)
    time.sleep(3)    

def Output(thruster,speed):
    pi.set_servo_pulsewidth(pin_array[thruster],speed)
    
def Output_All(speed):
    for i in pin_array:
        pi.set_servo_pulsewidth(i, speed)

def End():
    Output_All(1500)
    time.sleep(1)
    
    pi.stop()


