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

class Projectt:
    def __init__(self, name,  HEIGHT, WIDTH, bgc, vr_icon, canvas, root, signUpWindow, vr_image, setEmailWindow, upload_window, name_variable):
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



    def camera(self):
        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
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


    def voice_input(self):
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=0)
        with mic as source:
          r.adjust_for_ambient_noise(source, duration=0)
          print("What is your name: ")
          audio = r.listen(source, timeout=0)
          print("Wait till your voice is recognised......\n")
          d=r.recognize_google(audio)
          self.name.insert(0, d)
      


    def starrt(self):
        self.HEIGHT = 2048 
        self.WIDTH = 2048
        self.bgc='lightyellow'
        
        #self.root = tk.Tk()
        self.root.title('TRACK SMART Attendence System')
        
        #this to define canvas in GUI
        self.canvas = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH, bg='lightpink')
        self.canvas.pack()

        '''
        self.canvas = tk.Toplevel(self.root, height=self.HEIGHT, width=self.WIDTH, bg='lightpink')
        #self.canvas.title('SIGN UP for TRACK SMART Attendence')
    
        '''

        #photoimage for icon
        self.vr_image = tk.PhotoImage(file = "vr_icon.png")
        self.vr_icon = self.vr_image.subsample(11,11)




    def remainn(self):
        self.root.destroy()
        self.root=tk.Tk()
        self.root.title('TRACK SMART Attendence System')
        
        #this to define canvas in GUI
        self.canvas = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH, bg='lightpink')
        self.canvas.pack()


        #to print welcome message
        welcomeMsg = tk.Message(self.canvas, text='WELCOME TO SMART TRACK ATTENDENCE SYSTEM')
        welcomeMsg.config(bg='lightpink', font=('times', 48, 'italic'))
        welcomeMsg.place(relx= 0.05, rely=0.05, relwidth=0.4, relheight=0.9)

        #button for new user
        signUpBtn = tk.Button(self.canvas, text="SIGN UP", font=('times', 36), command=self.signUp)
        signUpBtn.place(relx=0.6, rely=0.35, relheight=0.08, relwidth=0.15)

        #button for existing student
        signInBtn = tk.Button(self.canvas, text="SIGN IN", font=('times', 36), command=self.signIn)
        signInBtn.place(relx=0.6, rely=0.55, relheight=0.08, relwidth=0.15)

        

    def submittedScreen(self):
                        self.root.destroy()
                        self.root=tk.Tk()
                        congoWindow = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH)
                        congoWindow.pack()
                        self.root.title('CONGRATULATIONS')
                        congoMsg = tk.Message(congoWindow, text='Congratulations...\nYou are successfully registered\nwith\nTRACK SMART ATTENDENCE SYSTEM')
                        congoMsg.config(justify='center', font=('times', 52, 'italic'))
                        congoMsg.place(relx= 0.05, rely=0.075, relwidth=0.9, relheight=0.6)

                        exitBtn = tk.Button(congoWindow, text="GO TO WELCOME SCREEN", font=('times', 36), command=self.remainn)
                        exitBtn.place(relx=0.31,  rely=0.75, relheight=0.075, relwidth=0.38)



    def confirm_submit(self):
                        email_label = tk.Label(self.setEmailWindow, text="Are you sure you want to continue?", font=('times', 36))
                        email_label.place(rely=0.5, relwidth=1)

                        confirmationFinal = tk.Label(self.setEmailWindow, text="You won't be able to change it later.", font=('times', 36))
                        confirmationFinal.place(rely=0.6, relwidth=1)

                        

                        finalButton = tk.Button(self.setEmailWindow, text="CONFIRM", font=('times', 36), command=self.submittedScreen)
                        finalButton.place(relx=0.75, rely=0.8, relwidth = 0.15)

                        backButton = tk.Button(self.setEmailWindow, text="BACK", font=('times', 36), command=self.toPasswordScreen)
                        backButton.place(relx=0.1, rely=0.8, relwidth = 0.15)


    
    def toEmailScreen(self):
                    self.root.destroy()
                    self.root=tk.Tk()
                    self.setEmailWindow = tk.Canvas(self.root,height=self.HEIGHT, width=self.WIDTH)
                    self.root.title('SET EMAIL')
                    self.setEmailWindow.pack()
                    
                    emailMsg = tk.Label(self.setEmailWindow, text="Please enter your email-ID below", font=('times', 36))
                    emailMsg.place(rely=0.15, relwidth=1)

                    email = tk.Entry(self.setEmailWindow, font=('times', 36))
                    email.place(rely=0.3, relx=0.13, relwidth=0.50, relheight=0.08)

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
            upload_label = tk.Label(self.upload_window, text="Upload Your Image for Face Recognistion", font=('times', 36))
            upload_label.place(rely=0.2, relwidth=1)

            webcam_button = tk.Button(self.upload_window, text="WEBCAM", font=('times', 36), command=self.camera)
            webcam_button.place(relx=0.4, rely=0.4, relwidth=0.2)

            upload_button = tk.Button(self.upload_window, text="UPLOAD", font=('times', 36), command=self.openn)
            upload_button.place(relx=0.4, rely=0.55, relwidth=0.2)

            proceed_button = tk.Button(self.upload_window, text="PROCEED", font=('times', 36), command=self.toPasswordScreen)
            proceed_button.place(relx=0.75, rely=0.8, relwidth=0.15)

            back_button = tk.Button(self.upload_window, text="BACK", font=('times', 36), command=self.signUp)
            back_button.place(relx=0.1, rely=0.8, relwidth=0.15)
            



    def goToWlcmScreen():
                            self.signUpWindow.destroy()
                            upload_window.destroy()
                            setPasswordWindow.destroy()
                            setEmailWindow.destroy()
                            congoWindow.destroy()
                            setEmailWindow.destroy()

    #def congo_screen():

                        
                        
    def destroy_ew():
                        setEmailWindow.destroy()


    #def email_screen():
    def destroy_pw():
                    setPasswordWindow.destroy()


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

            yesButton = tk.Button(self.signUpWindow, text="CONFIRM", font=('times', 36), command=self.imgUploadScreen)
            yesButton.place(relx=0.75, rely=0.8, relwidth = 0.15)


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
    def signIn():
        signInWindow = tk.Toplevel(height=HEIGHT, width=WIDTH)
        signInWindow.title('SIGN IN for TRACK SMART Attendence')

        welcomeUser = tk.Label(signInWindow, text="Welcome User,\n\nPlease say your passcode...", font=('times', 36))
        welcomeUser.place(rely=0.2, relwidth=1)

    def mainn(self):

        #to print welcome message
        welcomeMsg = tk.Message(self.canvas, text='WELCOME TO SMART TRACK ATTENDENCE SYSTEM')
        welcomeMsg.config(bg='lightpink', font=('times', 48, 'italic'))
        welcomeMsg.place(relx= 0.05, rely=0.05, relwidth=0.4, relheight=0.9)

        #button for new user
        signUpBtn = tk.Button(self.canvas, text="SIGN UP", font=('times', 36), command=self.signUp)
        signUpBtn.place(relx=0.6, rely=0.35, relheight=0.08, relwidth=0.15)

        #button for existing student
        signInBtn = tk.Button(self.canvas, text="SIGN IN", font=('times', 36), command=self.signIn)
        signInBtn.place(relx=0.6, rely=0.55, relheight=0.08, relwidth=0.15)

        #self.root.mainloop()




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

p=Projectt(name,HEIGHT, WIDTH, bgc, vr_icon, canvas, root, signUpWindow, vr_image, setEmailWindow, upload_window, name_variable)
p.starrt()
#p.signUp()
p.mainn()
#print(p.name_variable)
#print(p.name.get())
