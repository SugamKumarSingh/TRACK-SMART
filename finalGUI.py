import tkinter as tk

HEIGHT = 2048
WIDTH = 2048
bgc='lightyellow'

root = tk.Tk()
root.title('TRACK SMART Attendence System')

#this to define canvas in GUI
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='lightpink')
canvas.pack()

#photoimage for icon
vr_image = tk.PhotoImage(file = "vr_icon.png")
vr_icon = vr_image.subsample(11,11)

#function for signup
def signUp():
    signUpWindow = tk.Toplevel(height=HEIGHT, width=WIDTH, bg=bgc)
    signUpWindow.title('SIGN UP for TRACK SMART Attendence')

    #to confirm name from user
    def confirm_name():
        name_label = tk.Label(signUpWindow, bg=bgc, text="You entered  \"" + name.get() + "\"", font=('times', 36))
        name_label.place(rely=0.5, relwidth=1)
	
        confirmation = tk.Label(signUpWindow, bg=bgc, text="Are you sure you want to continue ?", font=('times', 36))
        confirmation.place(rely=0.6, relwidth=1)

        backButton = tk.Button(signUpWindow, text="RETAKE", font=('times', 36), command=relaunchSignUp)
        backButton.place(relx=0.1, rely=0.8, relwidth = 0.15)

        yesButton = tk.Button(signUpWindow, text="CONFIRM", font=('times', 36), command=imgUploadScreen)
        yesButton.place(relx=0.75, rely=0.8, relwidth = 0.15)

    #to upload ot click image for face recognistion
    def imgUploadScreen():
        upload_window = tk.Toplevel(height=HEIGHT, width=WIDTH)
        upload_window.title('UPLOAD IMAGE')

        def toPasswordScreen():
            setPasswordWindow = tk.Toplevel(height=HEIGHT, width=WIDTH)
            setPasswordWindow.title('SET PASSCODE')

            def toEmailScreen():
                setEmailWindow = tk.Toplevel(height=HEIGHT, width=WIDTH)
                setEmailWindow.title('SET EMAIL')

                def confirm_submit():
                    email_label = tk.Label(setEmailWindow, text="Are you sure you want to continue?", font=('times', 36))
                    email_label.place(rely=0.5, relwidth=1)

                    confirmationFinal = tk.Label(setEmailWindow, text="You won't be able to change it later.", font=('times', 36))
                    confirmationFinal.place(rely=0.6, relwidth=1)

                    backButton = tk.Button(setEmailWindow, text="BACK", font=('times', 36), command=destroy_ew)
                    backButton.place(relx=0.1, rely=0.8, relwidth = 0.15)

                    finalButton = tk.Button(setEmailWindow, text="CONFIRM", font=('times', 36), command=submittedScreen)
                    finalButton.place(relx=0.75, rely=0.8, relwidth = 0.15)

                def submittedScreen():
                    congoWindow = tk.Toplevel(height=HEIGHT, width=WIDTH)
                    congoWindow.title('CONGRATULATIONS')

                    def goToWlcmScreen():
                        signUpWindow.destroy()
                        upload_window.destroy()
                        setPasswordWindow.destroy()
                        setEmailWindow.destroy()
                        congoWindow.destroy()
                        setEmailWindow.destroy()

                    congoMsg = tk.Message(congoWindow, text='Congratulations...\nYou are successfully registered\nwith\nTRACK SMART ATTENDENCE SYSTEM')
                    congoMsg.config(justify='center', font=('times', 52, 'italic'))
                    congoMsg.place(relx= 0.05, rely=0.075, relwidth=0.9, relheight=0.6)

                    exitBtn = tk.Button(congoWindow, text="GO TO WELCOME SCREEN", font=('times', 36), command=goToWlcmScreen)
                    exitBtn.place(relx=0.31,  rely=0.75, relheight=0.075, relwidth=0.38)
                    
                def destroy_ew():
                    setEmailWindow.destroy()

                emailMsg = tk.Label(setEmailWindow, text="Please enter your email-ID below", font=('times', 36))
                emailMsg.place(rely=0.15, relwidth=1)

                email = tk.Entry(setEmailWindow, font=('times', 36))
                email.place(rely=0.3, relx=0.13, relwidth=0.50, relheight=0.08)

                email_button = tk.Button(setEmailWindow, text="SUBMIT Email", font=('times', 36), command=confirm_submit)
                email_button.place(relx=0.68, rely=0.3, relwidth=0.18, relheight=0.08)                

            def destroy_pw():
                setPasswordWindow.destroy()

            pswd = tk.Label(setPasswordWindow, text="Please set your Passcode by pressing the button below", font=('times', 36))
            pswd.place(rely=0.15, relwidth=1)

            vrPasscode = tk.Button(setPasswordWindow, image = vr_image, font=('times', 36))
            vrPasscode.place(relx=0.4, rely=0.3, width=300, height=400)

            proceed_button = tk.Button(setPasswordWindow, text="PROCEED", font=('times', 36), command=toEmailScreen)
            proceed_button.place(relx=0.75, rely=0.8, relwidth=0.15)

            back_button = tk.Button(setPasswordWindow, text="BACK", font=('times', 36), command=destroy_pw)
            back_button.place(relx=0.1, rely=0.8, relwidth=0.15)

        def destroy_uw():
            upload_window.destroy()

        upload_label = tk.Label(upload_window, text="Upload Your Image for Face Recognistion", font=('times', 36))
        upload_label.place(rely=0.2, relwidth=1)

        webcam_button = tk.Button(upload_window, text="WEBCAM", font=('times', 36))
        webcam_button.place(relx=0.4, rely=0.4, relwidth=0.2)

        upload_button = tk.Button(upload_window, text="UPLOAD", font=('times', 36))
        upload_button.place(relx=0.4, rely=0.55, relwidth=0.2)

        proceed_button = tk.Button(upload_window, text="PROCEED", font=('times', 36), command=toPasswordScreen)
        proceed_button.place(relx=0.75, rely=0.8, relwidth=0.15)

        back_button = tk.Button(upload_window, text="BACK", font=('times', 36), command=destroy_uw)
        back_button.place(relx=0.1, rely=0.8, relwidth=0.15)

    def relaunchSignUp():
        signUpWindow.destroy()
        signUp()

    #here i have added frame to our GUI for name entry
    entryFrame = tk.Frame(signUpWindow, bg=bgc, bd=10)
    entryFrame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.1, anchor='n')

    #entry field for name
    name = tk.Entry(entryFrame, font=('times', 36))
    name.place(relwidth=0.6, relheight=1)

    #button for voice recognition
    vr_button = tk.Button(entryFrame, image = vr_icon)
    vr_button.place(relx=0.64, relheight=1, relwidth=0.07)

    #button for name
    name_button = tk.Button(entryFrame, text="SUBMIT Name", font=('times', 36), command=confirm_name)
    name_button.place(relx=0.75, relheight=1, relwidth=0.25)

#function for signin
def signIn():
    signInWindow = tk.Toplevel(height=HEIGHT, width=WIDTH)
    signInWindow.title('SIGN IN for TRACK SMART Attendence')

    welcomeUser = tk.Label(signInWindow, text="Welcome User,\n\nPlease say your passcode...", font=('times', 36))
    welcomeUser.place(rely=0.2, relwidth=1)

#to print welcome message
welcomeMsg = tk.Message(canvas, text='WELCOME TO SMART TRACK ATTENDENCE SYSTEM')
welcomeMsg.config(bg='lightpink', font=('times', 48, 'italic'))
welcomeMsg.place(relx= 0.05, rely=0.05, relwidth=0.4, relheight=0.9)

#button for new user
signUpBtn = tk.Button(canvas, text="SIGN UP", font=('times', 36), command=signUp)
signUpBtn.place(relx=0.6, rely=0.35, relheight=0.08, relwidth=0.15)

#button for existing student
signInBtn = tk.Button(canvas, text="SIGN IN", font=('times', 36), command=signIn)
signInBtn.place(relx=0.6, rely=0.55, relheight=0.08, relwidth=0.15)

root.mainloop()