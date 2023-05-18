import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",0,255,empty)
cv2.createTrackbar("Threshold2","Parameters",0,255,empty)
cv2.createTrackbar("Area","Parameters",5000,30000,empty)
# cv2.createTrackbar("HUE Min", "Parameters", 0, 180, empty)
# cv2.createTrackbar("HUE Max", "Parameters", 0, 255, empty)
# cv2.createTrackbar("SAT Min", "Parameters", 0, 180, empty)
# cv2.createTrackbar("SAT Max", "Parameters", 0, 255, empty)
# cv2.createTrackbar("VALUE Min", "Parameters", 0, 180, empty)
# cv2.createTrackbar("VALUE Max", "Parameters", 0, 255, empty)

# def getContours(frame,frameContour):
def getContours(frame,frameContour):    
    contours,_ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
#         area =  cv2.contourArea(cnt)
#         
#         if area > 1000:
#             cv2.drawContours(frame, cnt, -1, (0, 255, 0), 3)
    
            area = cv2.contourArea(cnt)
            areaMin = cv2.getTrackbarPos("Area", "Parameters")
            if area > areaMin:
                cv2.drawContours(frameContour, cnt, -1, (255, 0, 255), 2)
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                print(len(approx))
                x , y , w, h = cv2.boundingRect(approx)
                cv2.rectangle(frameContour, (x , y ), (x + w , y + h ), (0, 255, 0), 3)

                cv2.putText(frameContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                            (0, 255, 0), 2)
                cv2.putText(frameContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 255, 0), 2)            
while True:
    ret, frame = cap.read()
    frameContour = frame.copy()
    
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    
#     threshold1 = cv2.getTrackbarPos("HUE Min", "Parameters")
#     threshold2 = cv2.getTrackbarPos("HUE Max", "Parameters")
#     threshold3 = cv2.getTrackbarPos("SAT Min", "Parameters")
#     threshold4 = cv2.getTrackbarPos("SAT Max", "Parameters")
#     threshold5 = cv2.getTrackbarPos("VALUE Min", "Parameters")
#     threshold6 = cv2.getTrackbarPos("VALUE Max", "Parameters")
    
    lower_red = np.array([200,0,0])
    upper_red = np.array([255,102,102])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask= mask)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    
    frameCanny = cv2.Canny(hsv, threshold1, threshold2)
    dilate = cv2.dilate(frameCanny, None, iterations = 1)
    getContours(dilate,frameContour)
    
    
    #cv2.imshow("Frame", frame)
    frame2 = cv2.flip(frame,-1)
    frame3 = cv2.flip(frameContour,-1)
    
    #cv2.imshow("Mask", mask)
    #cv2.imshow("Contours", frameContour)
    #cv2.imshow("Copy", frame2)
    cv2.imshow("Real Contour", frame3)
    
#     cv2.imshow("Contour", contours)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
    
cap.release()
cv2.destroyAllWindows()