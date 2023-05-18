import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((4,4), np.uint8) #increases/decrease the noise area of the detected objects

while(True):
    ret, frame = cap.read()
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converts the BGR values onto the HSV values of real colors
    red_lower = np.array([136,87,111], np.uint8) # numpy array for detecting the brighter color of red
    red_upper = np.array([180,255,255], np.uint8) # numpy array for detecting the darker color of red
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) # will only grab the colors above and "mask" them onto a seperate window
                                                            #(use cv2.imshow('Mask', red_mask) to view this)
    red_mask = cv2.dilate(red_mask, kernel) #dilates the mask to make the detection of the object clearer
    res_red = cv2.bitwise_and(frame, frame, mask = red_mask) # makes the mask much more clearer and smoother
      
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #contours the external portions of the objects
    if len(contours)>0:
        cv2.drawContours(frame, contours, -5, (0, 255, 0), 3) #contour lines will be green with a thickness of 3mm
        c = max(contours, key = cv2.contourArea) # makes the contours max out at the specific object range
        x,y,w,h = cv2.boundingRect(c) # internally calculates the area of the objects to be contoured
          
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
#     text = 'CPU Temperature'
#     text2 = '---------------------------------------------------------------------------------------------------------------------------------------------------------------'
#     text3 = '---------------------------------------------------------------------------------------------------------------------------------------------------------------'
#     coordinates = (0,50)
#     coordinates2 = (0,225)
#     coordinates3 = (10,225)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     fontScale = 1
#     color = (255,0,255)
#     thickness = 1
    frame2 = cv2.flip(frame,-1) # flips the original camera view 180 degrees
#     frame2 = cv2.putText(frame2, text, coordinates, font, fontScale, color, thickness, cv2.LINE_AA)
#     frame2 = cv2.putText(frame2, text2, coordinates2, font, fontScale, color, thickness, cv2.LINE_AA)
#     frame2 = cv2.putText(frame2, text3, coordinates3, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('Window', frame2) #outputs the flipped camera view
    #cv2.imshow('Frame', frame) creates the frame window for camera view
    if cv2.waitKey(10) & 0xFF == ord('q'): # keys to stop the program
        break

# cap.release() 
cv2.destroyAllWindows()