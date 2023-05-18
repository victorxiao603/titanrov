from time import sleep

def Init():
    
    global prev_speeds
    prev_speeds = [0,0,0,0,0,0] #[F_L,B_L,L,F_R,B_R,R]
    global prev_speeds_2
    prev_speeds_2 = [0,0,0,0,0,0] #[F_L,B_L,L,F_R,B_R,R]
    
    global prev_directions
    prev_directions = [0,0,0,0,0,0] #[F_L,B_L,L,F_R,B_R,R]
    
    global flip_times
    flip_times = [0,0,0,0,0,0]
    
    global new_dir
    new_dir = 0
    
# def PrintPrev():
#     print("prev speeds:" + str(prev_speeds))
#     print("prev dirs:" + str(prev_directions))
#     print("flip times:" + str(flip_times))
    
def Adjust(x, speed, direction):
    
    movement = 1500
    
    if (speed == 0) and (prev_speeds[x] > 0):
        flip_times[x] = int((prev_speeds[x] + prev_speeds_2[x])/2)
        prev_speeds_2[x] = prev_speeds[x]
        prev_speeds[x] = speed

    if ((prev_speeds[x] > 0) and (not(direction == prev_directions[x]))):
        flip_times[x] = int((prev_speeds[x] + prev_speeds_2[x])/2)
        prev_speeds_2[x] = prev_speeds[x]
        prev_speeds[x] = 0

        
    elif (not (flip_times[x] > 0)) or (direction == prev_directions[x]):
        
        if (direction == 1):
            movement = movement + speed
        else:
            movement = movement - speed
        
        prev_speeds_2[x] = prev_speeds[x]
        prev_speeds[x] = speed
        
        prev_directions[x] = direction  

      
    if (flip_times[x] > 0):
        flip_times[x] = flip_times[x] - 30
        
    
    
    return movement

def Invert(speed):
    
    nspeed = speed
    
    if speed > 1600:
        nspeed = 1600
    elif speed < 1400:
        nspeed = 1400
    
    if speed == 1500:
        return 1500
    
    elif nspeed > 1500:
        return 1500 - (nspeed - 1500)
    
    else:
        return 1500 + (1500 - nspeed)
