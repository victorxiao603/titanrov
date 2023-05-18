import ROV_Camera
import ROV_Controller
import ROV_Thruster
import ROV_Arm
#import ROV_OpenCV_Camera
from time import sleep

NUETRAL = 1500
MAX_FORWARD = 2000
MAX_BACKWARD = 1000
MODERATE_FORWARD = 1700

def main():
     
    print("\n\n")
    print("Starting initialization\n")
    print("Initializing controller")
    ROV_Controller.Init()
    print("Controller initialization success\n")
    
    
    print("Press down on both triggers to initialize the camera and arm")
    print("Hold down on the center Xbox button while pressing the tiggers to calibrate the motors")
    print("Motors need to be calibrated when first being powered on\n")
    
    # Loop that waits for both triggers to be pressed for at least 100ms before continuing 
    init_trgr = 0
    while(init_trgr == 0):
        init_trgr = ROV_Controller.Init_Trigger()
        sleep(0.1)
    
    print("Initializing motors")
    ROV_Thruster.Init()
    print("Thruster initialization success\n")
    
    print("Initializing claw")
    ROV_Arm.Init()
    print("Claw initialization success\n")
    
    # Checks if the center Xbox button was being pressed
    if (ROV_Controller.XBox_Button() == 1):
        print("Calibrating motors (Incoming beeping noises)")
        ROV_Thruster.Calibrate()
        print("Motor calibration sucess\n")
    
    print("Initializing camera")
    ROV_Camera.Init() 
    print("Camera initialization success\n")
    
    ROV_Camera.UpdateOverlay()
    
    # Main loop
    end_btn = 0
    while end_btn == 0:
        
        sleep(0.1) #time difference between each loop
        
        inputs = ROV_Controller.Input() # Returns array of adjusted inputs safe for the motors to output            

        if (ROV_Controller.Sprint_Button() == 1): # Outputs all motors at a moderate speed
            inputs = [MODERATE_FORWARD,MODERATE_FORWARD,MODERATE_FORWARD,MODERATE_FORWARD,MODERATE_FORWARD,MODERATE_FORWARD]  
        
        if (ROV_Controller.A_Button() == 1):
            ROV_Arm.Open_Close()
        
        for i in range(6):
            ROV_Thruster.Output(i,inputs[i])
        
        if (ROV_Controller.B_Button() == 1): 
            print("Testing motors")
            for i in range(6):
                print(i)
                ROV_Thruster.Output(i,MAX_FORWARD)
                sleep(2)
                ROV_Thruster.Output(i,NUETRAL)
            print("")
        
        if (ROV_Controller.X_Button()):
            ROV_Camera.UpdateOverlay()
        
        # If the back button is pressed the program ends
        end_btn = ROV_Controller.Y_Button()
    
    # End main loop
    print("Ending program")
    ROV_Camera.End()
    ROV_Thruster.End()
    ROV_Arm.End()
    
    sleep(1)
    print("Program ended sucessfully")
    
if __name__ == "__main__":
    main()