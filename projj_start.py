import tkinter as tk
import speech_recognition as sr
import os
from gtts import gTTS
from tkinter.filedialog import askopenfilename
from PIL import Image
import pyrebase
from tkinter import Tk
import face_recognition
from PIL import Image, ImageDraw
from shutil import copyfile
import cv2
from pathlib import Path
import shutil
import pathlib
import pandas as pd
import time 
from datetime import datetime, timedelta
from datetime import date
import smtplib
from openpyxl import load_workbook
from PIL import Image, ImageTk

class Projectt:
    def __init__(self, name,  HEIGHT, WIDTH, bgc, vr_icon, canvas, root, signUpWindow, vr_image, setEmailWindow, upload_window, name_variable, num, fn, k, password_array, chances, chances1, d1, setPasswordWindow, pazzword, pazzword_variable, emaill, emaill_variable):
        self.name=name
        self.HEIGHT=HEIGHT
        self.WIDTH=WIDTH
        self.bgc = bgc
        self.vr_icon=vr_icon
        self.canvas=canvas
        self.root=root=tk.Tk()
        self.signUpWindow=signUpWindow
        self.vr_image=vr_image
        self.setEmailWindow=setEmailWindow
        self.upload_window=upload_window
        self.name_variable=name_variable
        self.num=num
        self.fn=fn
        self.k=k
        self.password_array=password_array
        self.chances=chances
        self.chances1=chances1
        self.d1=d1
        self.setPasswordWindow=setPasswordWindow
        self.pazzword=pazzword
        self.pazzword_variable=pazzword_variable
        self.emaill=emaill
        self.emaill_variable=emaill_variable

    '''\
    def remove_new_folders(self, d1):
        os.chdir('..')
        if os.path.exists(d1):
                shutil.rmtree(d1)'''

    def face_recognition_for_multiple_images(self):
        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                os.chdir(pathlib.Path(__file__).parent.absolute())
                result=cv2.imwrite("unknown.jpg", frame)
                cam.release()
                cv2.destroyAllWindows()

        direc=os.getcwd()
        os.chdir(direc)
                
        cam = cv2.VideoCapture(0)
        cam.set(3, 2048)
        cam.set(4, 2048)
        while cv2.waitKey(1):
            ret, frame = cam.read()
            if ret == False:
                break
            cv2.imshow("test", frame)
            #cv2.waitKey(1)
            cv2.setMouseCallback("test", click_event)


        pd=pathlib.Path(__file__).parent.absolute()
        #print(pd)
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
        #path_on_cloud="images"

        all_files = storage.list_files()
        for file in all_files:
                #print(file.name)
                self.d1=path
                os.chdir(self.d1)
                file.download_to_filename(file.name)

        filelist = [f for f in os.listdir(self.d1) if f.endswith(".xlsx")]
        for f in filelist:
            os.remove(os.path.join(self.d1,f))

        os.chdir('..')

        try:    
            #Add known images 
            image_of_person = face_recognition.load_image_file('unknown.jpg')
            person_face_encoding = face_recognition.face_encodings(image_of_person)[0]

            for file_name in os.listdir(self.d1):
                

                #Load the file
                newPic = face_recognition.load_image_file(file_name)

                #Search every detected face
                for face_encoding in face_recognition.face_encodings(newPic):


                    results = face_recognition.compare_faces([person_face_encoding], face_encoding, 0.5)

                    self.num=0
                    
                    #If match, show it
                    if results[0] == True:
                        #copyFile(file_name, "./img/saved" + file_name)
                        self.num=self.num+1
                        self.fn=Path(file_name).stem
                        #print("Hi"+ str(fn))

            os.remove('unknown.jpg')

        except:
            self.failed_signIn()
            os.remove('unknown.jpg')
            
        if(self.num==1):
            #print("Hi "+ str(fn))
            self.signIn()
            os.chdir('..')
            if os.path.exists(self.d1):
                shutil.rmtree(d1)
        else:
            self.failed_signIn()
            os.chdir('..')
            if os.path.exists(self.d1):
                shutil.rmtree(d1)

        


        os.chdir('..')
        if os.path.exists(self.d1):
                shutil.rmtree(d1)





    def camera(self):
        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                result=cv2.imwrite("unknown.jpg", frame)
                cam.release()
                cv2.destroyAllWindows()

        direc=pathlib.Path(__file__).parent.absolute()
        os.chdir(direc)
                
        cam = cv2.VideoCapture(0)
        cam.set(3, 2048)
        cam.set(4, 2048)
        while cv2.waitKey(1):
            ret, frame = cam.read()
            if ret == False:
                break
            cv2.imshow("Camera", frame)
            #cv2.waitKey(1)
            cv2.setMouseCallback("Camera", click_event)

        config = {
              "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL" : "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
                  }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage() 

        path_on_cloud = (str(self.name_variable)+".jpg")
        path_local=("unknown.jpg");
        storage.child(path_on_cloud).put(path_local)
        os.remove("unknown.jpg")
    




    def openn(self):
        Tk().withdraw() 
        filename = askopenfilename()
        config = {
              "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL" : "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
            }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage() 

        path_on_cloud = (str(self.name_variable)+".jpg")
        path_local=(filename);
        storage.child(path_on_cloud).put(path_local)



    
    def voice_output(self, mytext):      
    
        # Language in which you want to convert 
        language = 'en'
          
        # Passing the text and language to the engine,  
        # here we have marked slow=False. Which tells  
        # the module that the converted audio should  
        # have a high speed 
        myobj = gTTS(text="Your entered" + str(mytext), lang=language, slow=False) 
          
        # Saving the converted audio in a mp3 file named 
        # welcome
        d=os.getcwd()
        os.chdir(d)
        myobj.save("welcome.mp3") 

        # Playing the converted file
        #welcome = r'D:\voce\welcome.mp3'
        #os.system("mpg123" + welcome) 

        from playsound import playsound
        playsound("welcome.mp3")

        os.remove("welcome.mp3")



    def voice_outputt(self, mytext):      
    
            # Language in which you want to convert 
            language = 'en'
              
            # Passing the text and language to the engine,  
            # here we have marked slow=False. Which tells  
            # the module that the converted audio should  
            # have a high speed 
            myobj = gTTS(text=str(mytext), lang=language, slow=False) 
              
            # Saving the converted audio in a mp3 file named 
            # welcome
            d=os.getcwd()
            os.chdir(d)
            myobj.save("welcome1.mp3") 

            # Playing the converted file
            #welcome = r'D:\voce\welcome.mp3'
            #os.system("mpg123" + welcome) 

            from playsound import playsound
            playsound("welcome1.mp3")

            os.remove("welcome1.mp3")



    def voice_input(self):
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=0)
        with mic as source:
          r.adjust_for_ambient_noise(source, duration=0)
          #print("What is your name: ")
          self.voice_outputt("Speak now")
          audio = r.listen(source, timeout=0)
          print("Wait till your voice is recognised......\n")
          d=r.recognize_google(audio)
          self.name.insert(0, d)
      


    def starrt(self):
        self.HEIGHT = 2048 
        self.WIDTH = 2048
        self.bgc='lightyellow'

        self.root.destroy()

        self.root = tk.Tk()
        self.root.title('TRACK SMART Attendence System')
        
        #this to define canvas in GUI
        self.canvas = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH, bg='black')
        self.canvas.pack()

        '''
        self.canvas = tk.Toplevel(self.root, height=self.HEIGHT, width=self.WIDTH, bg='lightpink')
        #self.canvas.title('SIGN UP for TRACK SMART Attendence')
    
        '''

        #photoimage for icon
        self.vr_image = tk.PhotoImage(file = "vr_icon.png")
        self.vr_icon = self.vr_image.subsample(11,11)




    def remainn(self):
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        if os.path.exists('images'):
            shutil.rmtree('images')
        self.root.destroy()
        self.root=tk.Tk()
        self.root.title('TRACK SMART Attendence System')
        
        #this to define canvas in GUI
        self.canvas = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH, bg='black')
        self.canvas.pack()


        #to print welcome message
        welcomeMsg = tk.Message(self.canvas, text='WELCOME TO SMART TRACK ATTENDENCE SYSTEM')
        welcomeMsg.config(bg='lightpink', font=('times', 48, 'italic'))
        welcomeMsg.place(relx= 0.05, rely=0.05, relwidth=0.4, relheight=0.9)

        #button for new user
        signUpBtn = tk.Button(self.canvas, text="SIGN UP", font=('times', 36), command=self.signUp)
        signUpBtn.place(relx=0.6, rely=0.35, relheight=0.08, relwidth=0.15)

        #button for existing student
        signInBtn = tk.Button(self.canvas, text="SIGN IN", font=('times', 36), command=self.face_recognition_for_multiple_images)
        signInBtn.place(relx=0.6, rely=0.55, relheight=0.08, relwidth=0.15)

        image = Image.open("black_bioChem.jpg")
        photo = ImageTk.PhotoImage(image)

        wlcmLabel = tk.Label(image=photo)
        wlcmLabel.place(relx=0.1, rely=0.2, relwidth=0.36, relheight=0.6)


    def submittedScreen(self):
                        self.root.destroy()
                        self.root=tk.Tk()
                        congoWindow = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
                        congoWindow.pack()
                        #self.voice_outputt("Congratulations you are successfully registered with track smart attendance system")


                        self.root.title('CONGRATULATIONS')
                        congoMsg = tk.Message(congoWindow, text='Congratulations...\nYou are successfully registered\nwith\nTRACK SMART ATTENDENCE SYSTEM')
                        congoMsg.config(justify='center', font=('times', 52, 'italic'))
                        congoMsg.place(relx= 0.05, rely=0.075, relwidth=0.9, relheight=0.6)

                        exitBtn = tk.Button(congoWindow, text="GO TO WELCOME SCREEN", font=('times', 36), command=self.remainn)
                        exitBtn.place(relx=0.31,  rely=0.75, relheight=0.075, relwidth=0.38)




    def confirm_submit(self):
                        self.emaill_variable = ' '

                        self.emaill_variable = self.emaill.get()

                        email_label = tk.Label(self.setEmailWindow, text="Are you sure you want to continue?", font=('times', 36))
                        email_label.place(rely=0.5, relwidth=1)

                        confirmationFinal = tk.Label(self.setEmailWindow, text="You won't be able to change it later.", font=('times', 36))
                        confirmationFinal.place(rely=0.6, relwidth=1)

                        

                        finalButton = tk.Button(self.setEmailWindow, text="CONFIRM", font=('times', 36), command=lambda:[self.submittedScreen(),self.add_new_email()])
                        finalButton.place(relx=0.75, rely=0.8, relwidth = 0.15)

                        backButton = tk.Button(self.setEmailWindow, text="BACK", font=('times', 36), command=self.toPasswordScreen)
                        backButton.place(relx=0.1, rely=0.8, relwidth = 0.15)



    def confirm_submit2(self):
        self.pazzword_variable = ' '

        self.pazzword_variable = self.pazzword.get()
        email_label = tk.Label(self.setPasswordWindow, text="Are you sure you want to continue?", font=('times', 36), bg='lightyellow')
        email_label.place(rely=0.5, relwidth=1)

        confirmationFinal = tk.Label(self.setPasswordWindow, text="You won't be able to change it later.",
                                     font=('times', 36), bg='lightyellow')
        confirmationFinal.place(rely=0.6, relwidth=1)

        finalButton = tk.Button(self.setPasswordWindow, text="CONFIRM", font=('times', 36), command=lambda:[self.toEmailScreen(), self.add_new_password()])
        finalButton.place(relx=0.75, rely=0.8, relwidth=0.15)

        backButton = tk.Button(self.setPasswordWindow, text="BACK", font=('times', 36), command=self.imgUploadScreen)
        backButton.place(relx=0.1, rely=0.8, relwidth=0.15)



    def toEmailScreen(self):
                    self.root.destroy()
                    self.root=tk.Tk()
                    self.setEmailWindow = tk.Canvas(self.root,height=self.HEIGHT, width=self.WIDTH)
                    self.root.title('SET EMAIL')
                    self.setEmailWindow.pack()

                    self.voice_outputt("Input your email")
                    
                    emailMsg = tk.Label(self.setEmailWindow, text="Please enter your email-ID below", font=('times', 36))
                    emailMsg.place(rely=0.15, relwidth=1)

                    self.emaill = tk.Entry(self.setEmailWindow, font=('times', 36))
                    self.emaill.place(rely=0.3, relx=0.13, relwidth=0.50, relheight=0.08)

                    email_button = tk.Button(self.setEmailWindow, text="SUBMIT Email", font=('times', 36), command=self.confirm_submit)
                    email_button.place(relx=0.68, rely=0.3, relwidth=0.18, relheight=0.08)                




    def reimgUploadScreen(self):
            self.root.destroy()
            self.root=tk.Tk()
            self.root.title('UPLOAD IMAGE')
            upload_window = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
            upload_window.pack()
            upload_label = tk.Label(upload_window, text="Upload Your Image for Face Recognistion", font=('times', 36))
            upload_label.place(rely=0.2, relwidth=1)

            webcam_button = tk.Button(upload_window, text="WEBCAM", font=('times', 36))
            webcam_button.place(relx=0.4, rely=0.4, relwidth=0.2)

            upload_button = tk.Button(upload_window, text="UPLOAD", font=('times', 36))
            upload_button.place(relx=0.4, rely=0.55, relwidth=0.2)

            proceed_button = tk.Button(upload_window, text="PROCEED", font=('times', 36), command=self.toPasswordScreen)
            proceed_button.place(relx=0.75, rely=0.8, relwidth=0.15)

            back_button = tk.Button(upload_window, text="BACK", font=('times', 36), command=self.signUp)
            back_button.place(relx=0.1, rely=0.8, relwidth=0.15)
            
   


    def toPasswordScreen(self):
                self.root.destroy()
                self.root=tk.Tk()
                setPasswordWindow = tk.Canvas(self.root,height=self.HEIGHT, width=self.WIDTH)
                self.root.title('SET PASSCODE')
                setPasswordWindow.pack()
                pswd = tk.Label(setPasswordWindow, text="Please set your Passcode by pressing the button below", font=('times', 36))
                pswd.place(rely=0.15, relwidth=1)

                #photoimage for icon
                self.vr_image = tk.PhotoImage(file = "vr_icon.png")
                self.vr_icon = self.vr_image.subsample(11,11)

                vrPasscode = tk.Button(setPasswordWindow, image = self.vr_image, font=('times', 36))
                vrPasscode.place(relx=0.4, rely=0.3, width=300, height=400)

                proceed_button = tk.Button(setPasswordWindow, text="PROCEED", font=('times', 36), command=self.toEmailScreen)
                proceed_button.place(relx=0.75, rely=0.8, relwidth=0.15)

                back_button = tk.Button(setPasswordWindow, text="BACK", font=('times', 36), command=self.imgUploadScreen)
                back_button.place(relx=0.1, rely=0.8, relwidth=0.15)


    def PasswordScreen(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title('SET PASSWORD')
        self.setPasswordWindow = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH, bg=self.bgc)
        self.setPasswordWindow.pack()

        # self.signUpWindow.title('SIGN UP for TRACK SMART Attendence')
        # here i have added frame to our GUI for name entry
        entryFrame = tk.Frame(self.setPasswordWindow, bg=self.bgc, bd=10)
        entryFrame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.1, anchor='n')

        # entry field for name
        self.pazzword = tk.Entry(entryFrame, font=('times', 36))
        self.pazzword.place(relwidth=0.6, relheight=1)

        self.voice_outputt("Input your password")
        '''
        self.vr_image = tk.PhotoImage(file="vr_icon.png")
        self.vr_icon = self.vr_image.subsample(11, 11)

        # button for voice recognition
        vr_button = tk.Button(entryFrame, image=self.vr_icon, )
        vr_button.place(relx=0.64, relheight=1, relwidth=0.07)
        '''

        # button for name
        name_button = tk.Button(entryFrame, text="SUBMIT Password", font=('times', 36), command = self.confirm_submit2)
        name_button.place(relx=0.65, relheight=1, relwidth=0.32)



    def resignUp(self):
        self.root.destroy()
        self.root=tk.Tk()
        self.root.title('SIGN UP for TRACK SMART Attendence')
        self.signUpWindow = tk.Canvas(self.root,height=self.HEIGHT, width=self.WIDTH, bg=self.bgc)
        self.signUpWindow.pack()
        #self.signUpWindow.title('SIGN UP for TRACK SMART Attendence')
                #here i have added frame to our GUI for name entry
        entryFrame = tk.Frame(self.signUpWindow, bg=self.bgc, bd=10)
        entryFrame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.1, anchor='n')

            #entry field for name
        self.name = tk.Entry(entryFrame, font=('times', 36))
        self.name.place(relwidth=0.6, relheight=1)

        self.vr_image = tk.PhotoImage(file = "vr_icon.png")
        self.vr_icon = self.vr_image.subsample(11,11)

            #button for voice recognition
        vr_button = tk.Button(entryFrame, image = self.vr_icon)
        vr_button.place(relx=0.64, relheight=1, relwidth=0.07)

            #button for name
        name_button = tk.Button(entryFrame, text="SUBMIT Name", font=('times', 36), command=self.confirm_name)
        name_button.place(relx=0.75, relheight=1, relwidth=0.25)
            


    def destroy_uw(self):
                self.resignUp


            #to upload ot click image for face recognistion
    def imgUploadScreen(self):
            self.root.destroy()
            self.root=tk.Tk()
            self.root.title('UPLOAD IMAGE')
            self.upload_window = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
            self.upload_window.pack()
            self.voice_outputt("Upload your image")
            upload_label = tk.Label(self.upload_window, text="Upload Your Image for Face Recognistion", font=('times', 36))
            upload_label.place(rely=0.2, relwidth=1)

            webcam_button = tk.Button(self.upload_window, text="WEBCAM", font=('times', 36), command=self.camera)
            webcam_button.place(relx=0.4, rely=0.4, relwidth=0.2)

            upload_button = tk.Button(self.upload_window, text="UPLOAD", font=('times', 36), command=self.openn)
            upload_button.place(relx=0.4, rely=0.55, relwidth=0.2)

            proceed_button = tk.Button(self.upload_window, text="PROCEED", font=('times', 36), command=self.PasswordScreen)
            proceed_button.place(relx=0.75, rely=0.8, relwidth=0.15)

            back_button = tk.Button(self.upload_window, text="BACK", font=('times', 36), command=self.signUp)
            back_button.place(relx=0.1, rely=0.8, relwidth=0.15)
            



    def goToWlcmScreen(self):
                            self.signUpWindow.destroy()
                            upload_window.destroy()
                            self.setPasswordWindow.destroy()
                            setEmailWindow.destroy()
                            self.congoWindow.destroy()
                            setEmailWindow.destroy()

    #def congo_screen():

                        
                        
    def destroy_ew(self):
                        setEmailWindow.destroy()


    #def email_screen():
    def destroy_pw(self):
                    self.setPasswordWindow.destroy()


    #def pw_screen():

                

    


                        
            
            




    def relaunchSignUp(self):
            self.signUpWindow.destroy()
            self.signUp()




    #to confirm name from user
    def confirm_name(self):
            self.name_variable= ' '

            self.name_variable=self.name.get()

            
        
            name_label = tk.Label(self.signUpWindow, bg=self.bgc, text="You entered \"" + str(self.name_variable)+'\"' , font=('times', 36))
            name_label.place(rely=0.5, relwidth=1)
            
            confirmation = tk.Label(self.signUpWindow, bg=self.bgc, text="Are you sure you want to continue ?", font=('times', 36))
            confirmation.place(rely=0.6, relwidth=1)

            backButton = tk.Button(self.signUpWindow, text="RETAKE", font=('times', 36), command=self.relaunchSignUp)
            backButton.place(relx=0.1, rely=0.8, relwidth = 0.15)

            yesButton = tk.Button(self.signUpWindow, text="CONFIRM", font=('times', 36), command=lambda: [
                self.add_new_name(), self.imgUploadScreen()])
            yesButton.place(relx=0.75, rely=0.8, relwidth = 0.15)



    #def add_new_email(self):





    def add_new_name(self):
        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()

        path_on_cloud = "demo.xlsx"
        # path_local=r'D:\lol\demo.xlsx';
        # storage.child(path_on_cloud).put(path_local)
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        #name = input("Enter your name - ")
        df = pd.DataFrame({'Name': [self.name_variable]})
        writer = pd.ExcelWriter('new.xlsx', engine='openpyxl')
        writer.book = load_workbook('new.xlsx')
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        reader = pd.read_excel('new.xlsx')
        df.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)
        writer.close()

        # firebase = pyrebase.initialize_app(config)
        # storage = firebase.storage()

        path_on_cloud = "demo.xlsx"
        path_local = "new.xlsx";
        storage.child(path_on_cloud).put(path_local)
        # d = os.getcwd
        # os.chdir(d)
        # storage.child(path_on_cloud).download("new.xlsx")
        os.remove("new.xlsx")



    def add_new_password(self):
        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()

        path_on_cloud = "demo.xlsx"
        # path_local=r'D:\lol\demo.xlsx';
        # storage.child(path_on_cloud).put(path_local)
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        #password = input("Enter your password - ")

        df = pd.read_excel('new.xlsx')

        df.loc[df['Name'] == self.name_variable, ['Password']] = str(self.pazzword_variable)

        df.to_excel('new.xlsx', index=False)

        path_on_cloud = "demo.xlsx"
        path_local = "new.xlsx";
        storage.child(path_on_cloud).put(path_local)
        # d = os.getcwd
        # os.chdir(d)
        # storage.child(path_on_cloud).download("new.xlsx")
        os.remove("new.xlsx")


    def add_new_email(self):
        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()

        path_on_cloud = "demo.xlsx"
        # path_local=r'D:\lol\demo.xlsx';
        # storage.child(path_on_cloud).put(path_local)
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        password = input("Enter your email - ")

        df = pd.read_excel('new.xlsx')

        df.loc[df['Name'] == self.name_variable, ['email']] = str(self.emaill_variable)

        df.to_excel('new.xlsx', index=False)

        path_on_cloud = "demo.xlsx"
        path_local = "new.xlsx";
        storage.child(path_on_cloud).put(path_local)
        # d = os.getcwd
        # os.chdir(d)
        # storage.child(path_on_cloud).download("new.xlsx")
        os.remove("new.xlsx")


    #function for signup
    def signUp(self):
        self.root.destroy()
        self.root=tk.Tk()
        self.root.title('SIGN UP for TRACK SMART Attendence')
        self.signUpWindow = tk.Canvas(self.root,height=self.HEIGHT, width=self.WIDTH, bg=self.bgc)
        self.signUpWindow.pack()

        #self.signUpWindow.title('SIGN UP for TRACK SMART Attendence')
                #here i have added frame to our GUI for name entry
        entryFrame = tk.Frame(self.signUpWindow, bg=self.bgc, bd=10)
        entryFrame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.1, anchor='n')

            #entry field for name
        self.name = tk.Entry(entryFrame, font=('times', 36))
        self.name.place(relwidth=0.6, relheight=1)

        self.voice_outputt("Input your name")
        

        self.vr_image = tk.PhotoImage(file = "vr_icon.png")
        self.vr_icon = self.vr_image.subsample(11,11)

            #button for voice recognition
        vr_button = tk.Button(entryFrame, image = self.vr_icon, command=self.voice_input)
        vr_button.place(relx=0.64, relheight=1, relwidth=0.07)

            #button for name
        name_button = tk.Button(entryFrame, text="SUBMIT Name", font=('times', 36), command=lambda:[self.voice_output(self.name.get()), self.confirm_name()])
        name_button.place(relx=0.75, relheight=1, relwidth=0.25)



   

    '''        #here i have added frame to our GUI for name entry
    entryFrame = tk.Frame(self.signUpWindow, bg=self.bgc, bd=10)
    entryFrame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.1, anchor='n')

        #entry field for name
    self.name = tk.Entry(entryFrame, font=('times', 36))
    self.name.place(relwidth=0.6, relheight=1)

        #button for voice recognition
    vr_button = tk.Button(entryFrame, image = self.vr_icon)
    vr_button.place(relx=0.64, relheight=1, relwidth=0.07)

        #button for name
    name_button = tk.Button(entryFrame, text="SUBMIT Name", font=('times', 36), command=self.signUp.confirm_name)
    name_button.place(relx=0.75, relheight=1, relwidth=0.25)
    '''
    #function for signin
    def signIn(self):

        self.chances = tk.IntVar()
        self.chances1= tk.IntVar()

        self.chances.set(3)
        self.chances1.set(self.chances.get())

        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        df = pd.read_excel('new.xlsx')

        x = []
        x = df[df['Name'] == self.fn]['Time']

        k = x[0]


        if(k==' '):
            self.root.destroy()
            self.root = tk.Tk()

            signInWindow = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
            self.root.title('SIGN IN for TRACK SMART Attendence')
            signInWindow.pack()

            welcomeUser = tk.Label(signInWindow, text="Welcome " + str(self.fn) + ",\n\nPlease say your passcode...",
                                   font=('times', 36))
            welcomeUser.place(rely=0.1, relwidth=1)

            self.vr_image = tk.PhotoImage(file="vr_icon.png")
            self.vr_icon = self.vr_image.subsample(11, 11)

            vrPasscode = tk.Button(signInWindow, image=self.vr_image, font=('times', 36), command=self.passwordd)
            vrPasscode.place(relx=0.4, rely=0.4, width=300, height=400)

            backButton = tk.Button(signInWindow, text="BACK", font=('times', 36), command=self.remainn)
            backButton.place(relx=0.1, rely=0.8, relwidth=0.15)

            config = {
                "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
                "authDomain": "tympass-32736.firebaseapp.com",
                "databaseURL": "https://tympass-32736.firebaseio.com",
                "projectId": "tympass-32736",
                "storageBucket": "tympass-32736.appspot.com",
                "messagingSenderId": "990276104410",
                "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
                "measurementId": "G-7HF9TQ5QC1"
            }
            firebase = pyrebase.initialize_app(config)
            storage = firebase.storage()
            path_on_cloud = "demo.xlsx"
            d = pathlib.Path(__file__).parent.absolute()
            os.chdir(d)
            storage.child(path_on_cloud).download("new.xlsx")

            df = pd.read_excel('new.xlsx')

            # name=input("Enter your name - ")

            self.password_array = []

            df.loc[df['Name'] == self.fn, ['Time']] = ' '

            df.to_excel('new.xlsx', index=False)

            config = {
                "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
                "authDomain": "tympass-32736.firebaseapp.com",
                "databaseURL": "https://tympass-32736.firebaseio.com",
                "projectId": "tympass-32736",
                "storageBucket": "tympass-32736.appspot.com",
                "messagingSenderId": "990276104410",
                "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
                "measurementId": "G-7HF9TQ5QC1"
            }
            firebase = pyrebase.initialize_app(config)
            storage = firebase.storage()
            path_on_cloud = "demo.xlsx"
            path_local = 'new.xlsx';
            storage.child(path_on_cloud).put(path_local)

            os.remove('new.xlsx')

        else:
            k_updated = pd.to_datetime(k)

        now = datetime.now()

        #print(now)
        #print(k_updated)

        if(k_updated<now):
            self.root.destroy()
            self.root = tk.Tk()

            signInWindow = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
            self.root.title('SIGN IN for TRACK SMART Attendence')
            signInWindow.pack()

            welcomeUser = tk.Label(signInWindow, text="Welcome " + str(self.fn) + ",\n\nPlease say your passcode...", font=('times', 36))
            welcomeUser.place(rely=0.1, relwidth=1)

            self.vr_image = tk.PhotoImage(file = "vr_icon.png")
            self.vr_icon = self.vr_image.subsample(11,11)

            vrPasscode = tk.Button(signInWindow, image = self.vr_image, font=('times', 36), command=self.passwordd)
            vrPasscode.place(relx=0.4, rely=0.4, width=300, height=400)

            backButton = tk.Button(signInWindow, text="BACK", font=('times', 36), command=self.remainn)
            backButton.place(relx=0.1, rely=0.8, relwidth = 0.15)

            config = {
                "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
                "authDomain": "tympass-32736.firebaseapp.com",
                "databaseURL": "https://tympass-32736.firebaseio.com",
                "projectId": "tympass-32736",
                "storageBucket": "tympass-32736.appspot.com",
                "messagingSenderId": "990276104410",
                "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
                "measurementId": "G-7HF9TQ5QC1"
            }
            firebase = pyrebase.initialize_app(config)
            storage = firebase.storage()
            path_on_cloud = "demo.xlsx"
            d = pathlib.Path(__file__).parent.absolute()
            os.chdir(d)
            storage.child(path_on_cloud).download("new.xlsx")

            df = pd.read_excel('new.xlsx')

            df.loc[df['Name'] == self.fn, ['Time']] = ' '

            df.to_excel('new.xlsx', index=False)

            config = {
                "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
                "authDomain": "tympass-32736.firebaseapp.com",
                "databaseURL": "https://tympass-32736.firebaseio.com",
                "projectId": "tympass-32736",
                "storageBucket": "tympass-32736.appspot.com",
                "messagingSenderId": "990276104410",
                "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
                "measurementId": "G-7HF9TQ5QC1"
            }
            firebase = pyrebase.initialize_app(config)
            storage = firebase.storage()
            path_on_cloud = "demo.xlsx"
            path_local = 'new.xlsx';
            storage.child(path_on_cloud).put(path_local)

            os.remove('new.xlsx')

        else:
            self.tryAgainScreen()





    def failed_signIn(self):
        self.root.destroy()
        self.root=tk.Tk()
        signInWindow = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
        self.root.title('SIGN IN for TRACK SMART Attendence')
        signInWindow.pack()

        welcomeUser = tk.Label(signInWindow, text="Sorry! Couldn't recognise you.", font=('times', 72))
        welcomeUser.place(rely=0.4, relwidth=1)


        backButton = tk.Button(signInWindow, text="BACK", font=('times', 36), command=self.remainn)
        backButton.place(relx=0.1, rely=0.8, relwidth = 0.15)

        cancelButton = tk.Button(signInWindow, text="EXIT", font=('times', 36), command=self.root.destroy)
        cancelButton.place(relx=0.75, rely=0.8, relwidth = 0.15)



    def welcome_button(self):
        HEIGHT = 2048
        WIDTH = 2048
        bgc = 'lightyellow'

        self.root.destroy()
        self.root = tk.Tk()
        self.root.title('TRACK SMART Attendence System')

        # this to define canvas in GUI
        canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH, bg='black')
        canvas.pack()

        btn_image = Image.open("black_bioChem.jpg")
        btn_photo = ImageTk.PhotoImage(btn_image)

        welcome_button = tk.Button(canvas, image=btn_photo, font=('times', 36), command = self.mainn)
        welcome_button.place(relx=0.32, rely=0.2, relwidth=0.34, relheight=0.6)

        self.root.mainloop()
        

    def mainn(self):

        #self.root.destroy()
        self.starrt()

        #to print welcome message
        welcomeMsg = tk.Message(self.canvas, text='WELCOME TO SMART TRACK ATTENDENCE SYSTEM')
        welcomeMsg.config(bg='black', font=('times', 48, 'italic'))
        welcomeMsg.place(relx= 0.05, rely=0.05, relwidth=0.4, relheight=0.9)

        #button for new user
        signUpBtn = tk.Button(self.canvas, text="SIGN UP", font=('times', 36), command=self.signUp)
        signUpBtn.place(relx=0.6, rely=0.35, relheight=0.08, relwidth=0.15)

        #button for existing student
        signInBtn = tk.Button(self.canvas, text="SIGN IN", font=('times', 36), command=self.face_recognition_for_multiple_images)
        signInBtn.place(relx=0.6, rely=0.55, relheight=0.08, relwidth=0.15)

        image = Image.open("black_bioChem.jpg")
        photo = ImageTk.PhotoImage(image)

        wlcmLabel = tk.Label(image=photo)
        wlcmLabel.place(relx=0.1, rely=0.2, relwidth=0.33, relheight=0.6)

        self.root.mainloop()




    def verifiedScreen(self):
                        self.root.destroy()
                        self.root=tk.Tk()
                        congoWindow = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
                        congoWindow.pack()
                        self.root.title('CONGRATULATIONS')
                        congoMsg = tk.Message(congoWindow, text='Congratulations...\nYou have been marked as\n PRESENT.')
                        congoMsg.config(justify='center', font=('times', 52, 'italic'))
                        congoMsg.place(relx= 0.05, rely=0.075, relwidth=0.9, relheight=0.6)

                        exitBtn = tk.Button(congoWindow, text="GO TO WELCOME SCREEN", font=('times', 36), command=self.mainn)
                        exitBtn.place(relx=0.31,  rely=0.75, relheight=0.075, relwidth=0.38)


    def unverifiedScreen(self):
                        self.root.destroy()
                        self.root=tk.Tk()
                        congoWindow = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
                        congoWindow.pack()
                        self.root.title('FAILURE')
                        congoMsg = tk.Message(congoWindow, text='Sorry...\nCouldn\'t understand \n Please Try Again.')
                        congoMsg.config(justify='center', font=('times', 52, 'italic'))
                        congoMsg.place(relx= 0.05, rely=0.075, relwidth=0.9, relheight=0.6)

                        exitBtn = tk.Button(congoWindow, text="RETRY", font=('times', 36), command=self.signIn)
                        exitBtn.place(relx=0.31,  rely=0.75, relheight=0.075, relwidth=0.38)


    def tryAgainTimeLimit(self):

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        # print("Current Time = ", current_time)

        # added_time = timedelta(minutes=15)

        updated_time = now + timedelta(minutes=15)

        updated_timee = updated_time.strftime("%H:%M:%S")

        #name = input("Enter your name - ")

        config = {
              "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL" : "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
            }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        df = pd.read_excel('new.xlsx')



        #name=input("Enter your name - ")

        self.password_array=[]

        df.loc[df['Name'] == self.fn, ['Time']] = str(updated_timee)

        df.to_excel('new.xlsx', index=False)

        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        path_local = 'new.xlsx';
        storage.child(path_on_cloud).put(path_local)

        os.remove('new.xlsx')

        # print("Updated time = ", updated_timee)

    def tryAgainScreen(self):
        self.root.destroy()
        self.root=tk.Tk()
        retryWindow = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
        retryWindow.pack()
        self.root.title('RETRY')
        backButton = tk.Button(retryWindow, text="BACK", font=('times', 36), command=self.remainn)
        backButton.place(relx=0.1, rely=0.8, relwidth=0.15)

        cancelButton = tk.Button(retryWindow, text="EXIT", font=('times', 36), command=self.root.destroy)
        cancelButton.place(relx=0.75, rely=0.8, relwidth=0.15)

        # define the countdown func. 
        def countdown(t):      
            while t: 
                mins, secs = divmod(t, 60) 
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                #self.root.destroy()
                
                retryMsg = tk.Message(retryWindow, text="Try again after \n" + timer + " \nminutes." + "\r" )
                retryMsg.config(justify='center', font=('times', 52, 'italic'))
                retryMsg.place(relx= 0.05, rely=0.075, relwidth=0.9, relheight=0.6)



                self.root.update()
                #exitBtn = tk.Button(retryWindow, text="GO TO WELCOME SCREEN", font=('times', 36))
                #exitBtn.place(relx=0.31,  rely=0.75, relheight=0.075, relwidth=0.38)
                time.sleep(1) 

                t -= 1
                
             
            #print('Fire in the hole!!') 
          
          
        # input time in seconds 
        #t = input("Enter the time in seconds: ") 
          
        # function call 
        #countdown(int(t)) 


        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        df = pd.read_excel('new.xlsx')


        x=[]
        x=df[df['Name']=='Swapnil Pant']['Time']

        k=x[0]

        k_updated=pd.to_datetime(k)

        diff = k_updated-now

        if(k_updated>now):
            countdown(int(diff.total_seconds()) )

        #else:
            #print('welcome')
        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        path_local = 'new.xlsx';
        storage.child(path_on_cloud).put(path_local)

        os.remove('new.xlsx')
        os.chdir('..')
        if os.path.exists(self.d1):
            shutil.rmtree(self.d1)



    def passwordd(self):
        config = {
              "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL" : "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
            }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        df = pd.read_excel('new.xlsx')



        #name=input("Enter your name - ")

        self.password_array=[]


        self.password_array=df[df['Name']==self.fn]['Password'].tolist()
        self.k=self.password_array[0]
        print(self.k)
        '''
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=0)
        with mic as source:
                  r.adjust_for_ambient_noise(source, duration=0)
                  #print("What is your name: ")
                  myobj = gTTS(text="Speak Now", lang='en', slow=False) 
                  
               
                  myobj.save("welcome.mp3") 

                

                  from playsound import playsound
                  playsound("welcome.mp3")

                  os.remove("welcome.mp3")
                  audio = r.listen(source, timeout=0)
                  #print("Wait till your voice is recognised......\n")
                  d=r.recognize_google(audio)
                  print(d)
                  #self.name.insert(0, d)
                  '''

        #print(self.chances.get())

        if(self.chances.get()>0):
            try:
                r = sr.Recognizer()
                mic = sr.Microphone(device_index=0)
                with mic as source:
                      r.adjust_for_ambient_noise(source, duration=0)
                      #print("What is your name: ")
                      myobj = gTTS(text="Speak Now", lang='en', slow=False)


                      myobj.save("welcome.mp3")



                      from playsound import playsound
                      playsound("welcome.mp3")

                      os.remove("welcome.mp3")
                      audio = r.listen(source, timeout=0)
                      #print("Wait till your voice is recognised......\n")
                      d=r.recognize_google(audio)
                      print(d)
                      #self.name.insert(0, d)

            except:
                myobj = gTTS(text="Sorry couldn not understand please speak again", lang='en', slow=False)

                myobj.save("welcome.mp3")

                from playsound import playsound
                playsound("welcome.mp3")

                os.remove("welcome.mp3")

            if (d==self.k):
                self.verifiedScreen()
                self.chances.set(self.chances.get()-1)
                self.chances1.set(self.chances.get())
                self.append_new_date_column()
                self.apply_present()
                self.sending_mail()
            elif(d!=self.k):
                #unverifiedScreen()
                #print('lol')
                myobj = gTTS(text="Wrong Password Speak Again.", lang='en', slow=False) 
                  
               
                myobj.save("welcome.mp3") 

                

                from playsound import playsound
                playsound("welcome.mp3")

                os.remove("welcome.mp3")
                self.chances.set(self.chances.get()-1)
                self.chances1.set(self.chances.get())
                
        elif(self.chances.get()==0):
                print(self.chances.get())
                self.tryAgainTimeLimit()
                self.tryAgainScreen()

        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        path_local = 'new.xlsx';
        storage.child(path_on_cloud).put(path_local)

        os.remove('new.xlsx')
        #path_local='new.xlsx'
        #storage.child(path_on_cloud).put(path_local)
        #os.remove('new.xlsx')


    def append_new_date_column(self):

        today = date.today()

        datee = today.strftime("%d/%m/%Y")

        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        df = pd.read_excel('new.xlsx')

        length = len(df.columns)

        try:
            df.insert(length, str(datee), "ABSENT")
            df.to_excel('new.xlsx', index=False)

        except:
            pass

        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        path_local = 'new.xlsx';
        storage.child(path_on_cloud).put(path_local)

        os.remove('new.xlsx')


    def apply_present(self):

        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        df = pd.read_excel('new.xlsx')

        today = date.today()

        datee = today.strftime("%d/%m/%Y")

        df.loc[df['Name'] == str(self.fn), [str(datee)]] = 'PRESENT'
        df.to_excel('new.xlsx', index=False)

        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        path_local = 'new.xlsx';
        storage.child(path_on_cloud).put(path_local)

        os.remove('new.xlsx')

    def sending_mail(self):

        config = {
            "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
            "authDomain": "tympass-32736.firebaseapp.com",
            "databaseURL": "https://tympass-32736.firebaseio.com",
            "projectId": "tympass-32736",
            "storageBucket": "tympass-32736.appspot.com",
            "messagingSenderId": "990276104410",
            "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
            "measurementId": "G-7HF9TQ5QC1"
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "demo.xlsx"
        d = pathlib.Path(__file__).parent.absolute()
        os.chdir(d)
        storage.child(path_on_cloud).download("new.xlsx")

        df = pd.read_excel('new.xlsx')

        today = date.today()

        datee = today.strftime("%d/%m/%Y")

        x = []
        x = df[df['Name'] == str(self.fn)][str(datee)]
        j = x[0]

        y = []
        y = df[df['Name'] == str(self.fn)]['email']
        k = y[0]

        print(k)
        print(j)

        yesterday = today - timedelta(days=1)
        yesterday_datee = yesterday.strftime("%d/%m/%Y")
        '''
        z = []
        z = df[df['Name'] == 'Swapnil Pant'][str(yesterday_datee)]
        l = z[0]
        '''
        p = 0

        if (j == 'PRESENT'):
            p = p + 1

        q = 0

        if (j == 'ABSENT'):
            q = q + 1

        # creates SMTP session
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        # start TLS for security
        # s.starttls()

        # Authentication
        s.login("tracksmartattendance@gmail.com", "12345678a@")

        # message to be sent
        message = ("You were present on " + str(datee) + ".")
        message1 = ("You were present on " + str(yesterday_datee) + ".")

        print(message)
        print(message1)

        print(p)
        print(q)

        if (p == 1):
            s.sendmail("tracksmartattendance@gmail.com", k, message)

        if (q == 1):
            s.sendmail("tracksmartattendance@gmail.com", k, message1)

        else:
            pass

        s.quit()

        os.remove('new.xlsx')


name=' '
HEIGHT = 0
WIDTH = 0
bgc=' '
vr_icon = ' '
canvas=' '
root=' '
signUpWindow= ' '
vr_image=' '
setEmailWindow= ' '
upload_window=' '
name_variable=' '
num=0
fn=' '
k=' '
password_array=' '
chances=0
chances1=0
d1=' '
setPasswordWindow=' '
pazzword=' '
pazzword_variable=' '
emaill=' '
emaill_variable=' '


p=Projectt(name,HEIGHT, WIDTH, bgc, vr_icon, canvas, root, signUpWindow, vr_image, setEmailWindow, upload_window, name_variable, num, fn, k, password_array, chances, chances1, d1, setPasswordWindow, pazzword, pazzword_variable, emaill, emaill_variable)
#p.starrt()
#p.signUp()
p.welcome_button()
#p.mainn()
d = pathlib.Path(__file__).parent.absolute()
os.chdir(d)
if os.path.exists('images'):
    shutil.rmtree('images') #only used
os.remove('new.xlsx')
#print(p.name_variable)
#print(p.name.get())
