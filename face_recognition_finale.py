import face_recognition
from PIL import Image, ImageDraw
from shutil import copyfile
import os
import cv2
from pathlib import Path
import shutil
import pyrebase

#num=0
'''
def import_images_in_a_folder():
    pd=os.getcwd()
    d='images'
    path=os.path.join(pd, d)
    mode=0o666
    os.mkdir(path, mode)

    config = {
              "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
              "authDomain": "tympass-32736.firebaseapp.com",
              "databaseURL" : "https://tympass-32736.firebaseio.com",
              "projectId": "tympass-32736",
              "storageBucket": "tympass-32736.appspot.com",
              "messagingSenderId": "990276104410",
              "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
              "measurementId": "G-7HF9TQ5QC1",
              "serviceAccount": "D:/lol/tympass-32736-firebase-adminsdk-73kvc-7991327d54.json"
              }
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    path_on_cloud="images"

    all_files = storage.list_files()
    for file in all_files:
        print(file.name)
        d1=path
        os.chdir(d1)
        file.download_to_filename(file.name)
        return d1
'''
def remove_new_folder(d1):
    os.chdir('..')
    if os.path.exists(d1):
            shutil.rmtree(d1)

def face_recognition_for_multiple_images():
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


        pd=os.getcwd()
        d='images'
        path=os.path.join(pd, d)
        mode=0o666
        os.mkdir(path, mode)

        config = {
                      "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
                      "authDomain": "tympass-32736.firebaseapp.com",
                      "databaseURL" : "https://tympass-32736.firebaseio.com",
                      "projectId": "tympass-32736",
                      "storageBucket": "tympass-32736.appspot.com",
                      "messagingSenderId": "990276104410",
                      "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
                      "measurementId": "G-7HF9TQ5QC1",
                      "serviceAccount": "D:/lol/tympass-32736-firebase-adminsdk-73kvc-7991327d54.json"
                      }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud="images"

        all_files = storage.list_files()
        for file in all_files:
                #print(file.name)
                d1=path
                os.chdir(d1)
                file.download_to_filename(file.name)

        os.chdir('..')

            
        #Add known images 
        image_of_person = face_recognition.load_image_file('unknown.jpg')
        person_face_encoding = face_recognition.face_encodings(image_of_person)[0]

        for file_name in os.listdir(d1):
            

            #Load the file
            newPic = face_recognition.load_image_file(file_name)

            #Search every detected face
            for face_encoding in face_recognition.face_encodings(newPic):


                results = face_recognition.compare_faces([person_face_encoding], face_encoding, 0.5)

                num=0
                
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


        remove_new_folder(d1)


face_recognition_for_multiple_images()
