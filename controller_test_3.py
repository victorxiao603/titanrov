from time import sleep
import pygame

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
RSTICK_BTN = 10
L_JOY_X = 0
L_JOY_Y = 1
L_T = 2
R_JOY_X = 3
R_JOY_Y = 4
R_T = 5



pygame.init()
joy1 = pygame.joystick.Joystick(0)
joy1.init()

def x_button():
    print("X")

def y_button():
    print("hello world")
    a = 1
    return a 

def main():

    btn_active = 0
    hats = joy1.get_numaxes()
    print(hats)
    while btn_active == 0:
        pygame.event.pump()
        hat = joy1.get_axis(R_JOY_Y)
        print("R_JOY_Y" + str(hat))
        h2 = joy1.get_axis(L_JOY_Y)
        print("L_JOY_Y"+str(h2))
        h1 = joy1.get_axis(L_JOY_X)
        print("L_JOY_Y"+str(h1))
        hat2 = joy1.get_axis(R_T)
        print("R_T" +str(hat2))
        
        h3 = joy1.get_axis(R_JOY_X)
        print("R_JOY_X"+str(h3))
        
        if joy1.get_button(Y_BTN) == 1:
            btn_active = y_button()
        if joy1.get_button(Y_BTN) == 0:
            print("AAAAAAAAAAAAAA")
        if joy1.get_button(X_BTN) == 1:
            print("X button pressed")
        if joy1.get_button(A_BTN) == 1:
            print("A button pressed")
        if joy1.get_button(B_BTN) == 1:
            print("B button pressed")
        if joy1.get_button(R_BTN) == 1:
            print("R  button pressed")
        if joy1.get_button(L_BTN) == 1:
            print("L button pressed")
        if joy1.get_button(START_BTN) == 1:
            print("Start button pressed")      
        if joy1.get_button(BOX_BTN) == 1:
            print("Start button pressed") 
        
        sleep(0.1)
        
    print("fin")

if __name__ == "__main__":
    main()