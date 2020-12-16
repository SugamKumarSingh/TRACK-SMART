import tkinter as tk
from tkinter import *
HEIGHT = 2048
WIDTH = 2048

root = tk.Tk()
root.title('TRACK SMART Attendence System')

#this to define canvas in GUI
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="lightgreen")
canvas.pack()

name_msg = tk.Message(canvas, text='WELCOME TO SMART TRACK ATTENDENCE SYSTEM')
name_msg.config(bg='lightgreen', font=('times', 48, 'italic'))
name_msg.place(relx= 0.09, relwidth=0.4, relheight=1)


#here i have added frame to our GUI for new user
frame = tk.Frame(root, bg='lightgreen', bd=10)
frame.place(relx=0.8, rely=0.35, relwidth=0.75, relheight=0.1, anchor='n')

sign_up = tk.Button(frame, text="SIGN UP", font=('times', 36))
sign_up.place(relx=0.25,rely=-0.45, relheight=2, relwidth=0.3)


#creating lower frame for email entry
lower_frame = tk.Frame(root, bg='lightgreen', bd=10)
lower_frame.place(relx=0.8, rely=0.55, relwidth=0.75, relheight=0.1, anchor='n')

#button for existing student
sign_in = tk.Button(lower_frame, text="SIGN IN", font=('times', 36))
sign_in.place(relx=0.25, rely=-0.45, relheight=2, relwidth=0.3)


root.mainloop()
