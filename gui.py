import tkinter as tk

HEIGHT = 500
WIDTH = 600

def test_function(name):
	print("This is the entry:", name)



root = tk.Tk()
root.title('SIGN UP for TRACK SMART Attendence')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
canvas.pack()



frame = tk.Frame(root, bg='white', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

name_msg = tk.Message(frame, text='Enter your name')
name_msg.config(bg='lightgreen', font=('times', 24, 'italic'))
name_msg.place(relwidth=0.65, relheight=1)


name = tk.Entry(frame, font=40)
name.place(relwidth=0.65, relheight=1)

name_button = tk.Button(frame, text="SUBMIT Name", font=40)
name_button.place(relx=0.7, relheight=1, relwidth=0.3)




lower_frame = tk.Frame(root, bg='white', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

email = tk.Entry(lower_frame, font=40)
email.place(relwidth=0.65, relheight=1)

email_button = tk.Button(lower_frame, text="SUBMIT Email", font=40)
email_button.place(relx=0.7, relheight=1, relwidth=0.3)




root.mainloop()







"""
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

def signup():
    print("SIGN UP")
    pass

def signin():
    print("SIGN IN")
    pass




canvas = tk.Canvas(root, height=500, width=700, bg='#ff4800')
canvas.pack()

frame = tk.Frame(root, bg='#9d00ff')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

new_student = tk.Button(frame, text='NEW STUDENT', activeforeground='red', padx=24, pady=10, fg='black', bg='gray', command=signup)
new_student.place(x=200, y=150)

existing_student = tk.Button(frame, text='EXISTING STUDENT', padx=10, pady=10, fg='black', bg='blue', command=signin)
existing_student.place(x=200, y=250)




root.mainloop()
"""