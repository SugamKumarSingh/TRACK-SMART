import cv2
import os

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        result=cv2.imwrite("unknown.jpg", frame)
        cam.release()
        cv2.destroyAllWindows()

direc=r'D:/lol'
os.chdir(direc)
        
cam = cv2.VideoCapture(0)
while cv2.waitKey(1):
    ret, frame = cam.read()
    if ret == False:
        break
    cv2.imshow("test", frame)
    #cv2.waitKey(1)
    cv2.setMouseCallback("test", click_event)
    

