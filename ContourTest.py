import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def empty(a):
    pass

cv2.namedWindow("Screen")
cv2.resizeWindow("Screen",120,4)
cv2.createTrackbar("HUE Min", "Screen", 47, 179, empty)
cv2.createTrackbar("HUE Max", "Screen", 179, 179, empty)
cv2.createTrackbar("SAT Min", "Screen", 101, 255, empty)
cv2.createTrackbar("SAT Max", "Screen", 255, 255, empty)
cv2.createTrackbar("VAL Min", "Screen", 0, 255, empty)
cv2.createTrackbar("VAL Max", "Screen", 255, 255, empty)

def getContours(frame, mask):
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        accuracy = 0.03*cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, accuracy, True)
        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 5)
        
while True:
    _, frame = cap.read()
    
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("HUE Min", "Screen")
    h_max = cv2.getTrackbarPos("HUE Max", "Screen")
    s_min = cv2.getTrackbarPos("SAT Min", "Screen")
    s_max = cv2.getTrackbarPos("SAT Max", "Screen")
    v_min = cv2.getTrackbarPos("VAL Min", "Screen")
    v_max = cv2.getTrackbarPos("VAL Max", "Screen")
    

    lower_red = np.array([h_min, s_min, v_min])
    upper_red = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Frame", frame)
    #cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()