from time import sleep
import pygame
import ROV_Movement

A_BTN = 0
B_BTN = 1
X_BTN = 2
Y_BTN = 3
L_BTN = 4
R_BTN = 5
BACK_BTN = 6
START_BTN = 7
BOX_BTN = 8
SPRINT_BTN = 9
L_JOY_X = 0
L_JOY_Y = 1
L_T = 2
R_JOY_X = 3
R_JOY_Y = 4
R_T = 5

F_L_m = 0
B_L_m = 1
L_m = 2
F_R_m = 3
B_R_m = 4
R_m = 5



def Init():
    pygame.init()
    ROV_Movement.Init()
      
    global ctrlr
    ctrlr = pygame.joystick.Joystick(0)
    ctrlr.init()
    
    global speeds
    speeds = [0,0,0,0,0,0] #[F_L,B_L,L,F_R,B_R,R]
    
    global directions
    directions = [1,1,1,1,1,1] #[F_L,B_L,L,F_R,B_R,R]

def Input():
    pygame.event.pump()
    
    # Get inputs to move the motors
    # Would recomend replacing with a better system
    
    movements = [1500,1500,1500,1500,1500,1500]
    
    rth = -1.0 
    rth = ctrlr.get_axis(R_T) # rth is -1 to 1
    rth += 1.0                # Sets it 0 to 2
    
    lth = -1.0 
    lth = ctrlr.get_axis(L_T) # -1 to 1
    lth += 1.0                # Sets it 0 to 2
    
    lxjh = ctrlr.get_axis(L_JOY_X)
    lyjh = ctrlr.get_axis(L_JOY_Y)
    rxjh = ctrlr.get_axis(R_JOY_X)
    ryjh = ctrlr.get_axis(R_JOY_Y)
    
    # Right and left trigger inputs
    if not ((rth > 0) and (lth > 0)):
            
        if (rth > 0): 
            speeds[L_m] = rth * 250 
            directions[L_m] = 1 
            speeds[R_m] = rth * 250 
            directions[R_m] = 1 
            
        elif (lth > 0): 
            speeds[L_m] = lth * 250
            directions[L_m] = 2
            speeds[R_m] = lth * 250
            directions[R_m] = 2
        else:
            speeds[L_m] = 0
            speeds[R_m] = 0
    else:
        speeds[L_m] = 0
        speeds[R_m] = 0
    
    # Right joystick X inputs
    if (rth == 0) and (lth == 0) and (not (rxjh == 0)):
        speeds[L_m] = abs(rxjh * 500)
        speeds[R_m] = abs(rxjh * 500)
        
        if (rxjh > 0):
            directions[L_m] = 1
            directions[R_m] = 2
        else:    
            directions[L_m] = 2
            directions[R_m] = 1
    
    # Left joystick Y inputs
    if not (lyjh == 0):
        speeds[F_L_m] = abs(lyjh * 500)
        speeds[F_R_m] = abs(lyjh * 500)
        speeds[B_L_m] = abs(lyjh * 500)
        speeds[B_R_m] = abs(lyjh * 500)
        
        # FORWARD AND BACKWARDS
        # forward on joystick is negative 
        if (lyjh > 0): 
            directions[F_L_m] = 2
            directions[F_R_m] = 1
            directions[B_L_m] = 1
            directions[B_R_m] = 2
        else:    
            directions[F_L_m] = 1
            directions[F_R_m] = 2
            directions[B_L_m] = 2
            directions[B_R_m] = 1
 
            
    # Left joystick X inputs
    elif not (lxjh == 0):
        speeds[F_L_m] = abs(lxjh * 500)
        speeds[F_R_m] = abs(lxjh * 500)
        speeds[B_L_m] = abs(lxjh * 500)
        speeds[B_R_m] = abs(lxjh * 500)
        
        # YAW RIGHT
        # right is positive 
        if (lxjh > 0):
            directions[F_L_m] = 1
            directions[F_R_m] = 1
            directions[B_L_m] = 2
            directions[B_R_m] = 2
        else:    
            directions[F_L_m] = 2
            directions[F_R_m] = 2
            directions[B_L_m] = 1
            directions[B_R_m] = 1
    
    elif (rth == 0) and (lth == 0) and (rxjh == 0) and (not (ryjh == 0)):
        speeds[L_m] = abs(ryjh * 200)
        speeds[R_m] = abs(ryjh * 200)
        directions[L_m] = 1
        directions[R_m] = 1
        
        if (ryjh < 0):
            speeds[F_L_m] = abs(ryjh * 500)
            speeds[F_R_m] = abs(ryjh * 500)    
            directions[F_L_m] = 1
            directions[F_R_m] = 2
        else:
            speeds[B_L_m] = abs(ryjh * 500)
            speeds[B_R_m] = abs(ryjh * 500)    
            directions[B_L_m] = 1
            directions[B_R_m] = 2
            
    elif ctrlr.get_button(L_BTN) == 1:
        speeds[F_L_m] = 500
        speeds[F_R_m] = 500
        speeds[B_L_m] = 500
        speeds[B_R_m] = 500
        
        directions[F_L_m] = 2
        directions[F_R_m] = 2
        directions[B_L_m] = 2
        directions[B_R_m] = 2
    
    elif ctrlr.get_button(R_BTN) == 1:
        speeds[F_L_m] = 500
        speeds[F_R_m] = 500
        speeds[B_L_m] = 500
        speeds[B_R_m] = 500
        
        directions[F_L_m] = 1
        directions[F_R_m] = 1
        directions[B_L_m] = 1
        directions[B_R_m] = 1
    
    else:
        speeds[F_L_m] = 0
        speeds[F_R_m] = 0
        speeds[B_L_m] = 0
        speeds[B_R_m] = 0

    
    movements[L_m] = ROV_Movement.Adjust(L_m,speeds[L_m],directions[L_m])
    movements[R_m] = ROV_Movement.Adjust(R_m,speeds[R_m],directions[R_m])
    movements[F_L_m] = ROV_Movement.Adjust(F_L_m,speeds[F_L_m],directions[F_L_m])
    movements[F_R_m] = ROV_Movement.Adjust(F_R_m,speeds[F_R_m],directions[F_R_m])
    movements[B_L_m] = ROV_Movement.Adjust(B_L_m,speeds[B_L_m],directions[B_L_m])
    movements[B_R_m] = ROV_Movement.Adjust(B_R_m,speeds[B_R_m],directions[B_R_m])
    
    #inverse functions here
    m1 = movements[L_m]
    m2 = movements[R_m]
    m3 = movements[F_L_m] 
    m4 = movements[B_L_m]
    m5 = movements[F_R_m]
    m6 = movements[B_R_m]
    
    movements[L_m] = ROV_Movement.Invert(m1)
    movements[R_m] = ROV_Movement.Invert(m2)
    movements[F_L_m] = ROV_Movement.Invert(m3)
    movements[B_L_m] = ROV_Movement.Invert(m4)
    movements[F_R_m] = ROV_Movement.Invert(m5)
    movements[B_R_m] = ROV_Movement.Invert(m6)

    return movements

def Init_Trigger():
    pygame.event.pump()
    if (ctrlr.get_axis(R_T) > 0) and (ctrlr.get_axis(L_T) > 0):
        return 1
    else:
        return 0

def XBox_Button():
    pygame.event.pump()
    if ctrlr.get_button(BOX_BTN) == 1:
        return 1
    else:
        return 0

def X_Button():
    pygame.event.pump()
    if ctrlr.get_button(X_BTN) == 1:
        return 1
    else:
        return 0

def B_Button():
    pygame.event.pump()
    if ctrlr.get_button(B_BTN) == 1:
        return 1
    else:
        return 0
    
def Start_Button():
    pygame.event.pump()
    if ctrlr.get_button(START_BTN) == 1:
        return 1
    else:
        return 0
    
def Back_Button():
    pygame.event.pump()
    return ctrlr.get_button(BACK_BTN)

def Sprint_Button():
    pygame.event.pump()
    if ctrlr.get_button(SPRINT_BTN) == 1:
        return 1
    else:
        return 0
    
def A_Button():
    pygame.event.pump()
    if ctrlr.get_button(A_BTN) == 1:
        return 1
    else:
        return 0    

def Y_Button():
    pygame.event.pump()
    if ctrlr.get_button(Y_BTN) == 1:
        return 1
    else:
        return 0
    
def Back_Button():
    pygame.event.pump()
    if ctrlr.get_button(BACK_BTN) == 1:
        return 1
    else:
        return 0    