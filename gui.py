import tkinter as tk

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

	def toPasswordScreen():
		setPasswordWindow = tk.Toplevel(height=HEIGHT, width=WIDTH)
		setPasswordWindow.title('SET PASSCODE')

		pswd = tk.Label(setPasswordWindow, text="Please set your Passcode by pressing the button below", font=('times', 36))
		pswd.place(rely=0.15, relwidth=1)

		vrPasscode = tk.Button(setPasswordWindow, image = vr_image, font=('times', 36))
		vrPasscode.place(relx=0.4, rely=0.3, width=300, height=400)

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
vr_button = tk.Button(frame, image = vr_icon)
vr_button.place(relx=0.64, relheight=1, relwidth=0.07)

#button for name
name_button = tk.Button(frame, text="SUBMIT Name", font=('times', 36), command=confirm_name)
name_button.place(relx=0.75, relheight=1, relwidth=0.25)



root.mainloop()