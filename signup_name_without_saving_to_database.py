import tkinter as tk
import speech_recognition as sr
import os
from gtts import gTTS

  

def voice_output(mytext):      
    
    # Language in which you want to convert 
    language = 'en'
      
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text="Your name has been saved as" + str(mytext), lang=language, slow=False) 
      
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

def voice_input():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    with mic as source:
      r.adjust_for_ambient_noise(source, duration=1)
      print("What is your name: ")
      audio = r.listen(source, timeout=0)
      print("Wait till your voice is recognised......\n")
      d=r.recognize_google(audio)
      name.insert(0, d)
      


HEIGHT = 2048
WIDTH = 2048
bgc='lightyellow'

root = tk.Tk()
root.title('SIGN UP for TRACK SMART Attendence')

#this to define canvas in GUI
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg=bgc)
canvas.pack()

#to upload ot click image for face recognistion
def next_screen():
	upload_window = tk.Toplevel(height=HEIGHT, width=WIDTH)
	upload_window.title('UPLOAD IMAGE')

	upload_label = tk.Label(upload_window, text="Upload Your Image for Face Recognistion", font=('times', 36))
	upload_label.place(rely=0.2, relwidth=1)

	webcam_button = tk.Button(upload_window, text="WEBCAM", font=('times', 36))
	webcam_button.place(relx=0.4, rely=0.4, relwidth=0.2)

	upload_button = tk.Button(upload_window, text="UPLOAD", font=('times', 36))
	upload_button.place(relx=0.4, rely=0.55, relwidth=0.2)


#to confirm name from user
def confirm_name():
	name_label = tk.Label(canvas, bg=bgc, text="You entered  \"" + name.get() + "\"", font=('times', 36))
	name_label.place(rely=0.5, relwidth=1)
	
	confirmation = tk.Label(canvas, bg=bgc, text="Are you sure you want to continue ?", font=('times', 36))
	confirmation.place(rely=0.6, relwidth=1)

	backButton = tk.Button(canvas, text="RETAKE", font=('times', 36))
	backButton.place(relx=0.1, rely=0.8, relwidth = 0.15)

	yesButton = tk.Button(canvas, text="CONFIRM", font=('times', 36), command=next_screen)
	yesButton.place(relx=0.75, rely=0.8, relwidth = 0.15)

#here i have added frame to our GUI for name entry
frame = tk.Frame(root, bg=bgc, bd=10)
frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.1, anchor='n')

#entry field for name
name = tk.Entry(frame, font=('times', 36))
name.place(relwidth=0.6, relheight=1)

#photoimage for icon
vr_image = tk.PhotoImage(file = "vr_icon.png")
vr_icon = vr_image.subsample(11,11)

#button for voice recognition
vr_button = tk.Button(frame, text="Voice Recognistion", image = vr_icon, font=('times', 36), command=voice_input)
vr_button.place(relx=0.64, relheight=1, relwidth=0.07)

#button for name
name_button = tk.Button(frame, text="SUBMIT Name", font=('times', 36), command=lambda:[confirm_name(), voice_output(name.get())])
name_button.place(relx=0.75, relheight=1, relwidth=0.25)



root.mainloop()

