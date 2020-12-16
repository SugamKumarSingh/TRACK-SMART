import tkinter as tk

HEIGHT = 2048
WIDTH = 2048

#this function is just an exaample to explain how to use assign function to buttons
def test_function(name):
	print("This is the entry:", name)

root = tk.Tk()
root.title('SIGN UP for TRACK SMART Attendence')

#this to define canvas in GUI
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="lightyellow")
canvas.pack()


#here i have added frame to our GUI for name entry
frame = tk.Frame(root, bg='lightyellow', bd=10)
frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.1, anchor='n')

#entry field for name
name = tk.Entry(frame, font=('times', 36))
name.place(relwidth=0.6, relheight=1)

#photoimage for icon
vr_image = tk.PhotoImage(file = "vr_icon.png")
vr_icon = vr_image.subsample(11,11)

#button for voice recognition
vr_button = tk.Button(frame, text="Voice Recognistion", image = vr_icon, font=('times', 36))
vr_button.place(relx=0.64, relheight=1, relwidth=0.07)

#button for name
name_button = tk.Button(frame, text="SUBMIT Name", font=('times', 36))
name_button.place(relx=0.75, relheight=1, relwidth=0.25)



root.mainloop()