import face_recognition
from PIL import Image, ImageDraw
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from shutil import copyfile
import os
import cv2
num=0
from pathlib import Path
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        result=cv2.imwrite("unknown.jpg", frame)
        cam.release()
        cv2.destroyAllWindows()

direc=os.getcwd()
os.chdir(direc)
        
cam = cv2.VideoCapture(0)
while cv2.waitKey(1):
    ret, frame = cam.read()
    if ret == False:
        break
    cv2.imshow("test", frame)
    #cv2.waitKey(1)
    cv2.setMouseCallback("test", click_event)
    
#Add known images 
image_of_person = face_recognition.load_image_file('unknown.jpg')
person_face_encoding = face_recognition.face_encodings(image_of_person)[0]

d=r'D:\lll'
#os.chdir(direc)

for file_name in os.listdir(d):
    #file_name = str(i).zfill(5) + ".jpg"
    #print(file_name)

    #Load the file
    newPic = face_recognition.load_image_file(file_name)

    #Search every detected face
    for face_encoding in face_recognition.face_encodings(newPic):


        results = face_recognition.compare_faces([person_face_encoding], face_encoding, 0.5)
         
        #If match, show it
        if results[0] == True:
            #copyFile(file_name, "./img/saved" + file_name)
            num=num+1
            fn=Path(file_name).stem
            #print("Hi"+ str(fn))

os.remove('unknown.jpg')
if(num==1):
    print("Hi "+ str(fn))
else:
    print("Sorry! Couldn't recognise you.")

