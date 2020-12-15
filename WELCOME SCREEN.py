import tkinter as tk

HEIGHT = 500
WIDTH = 700

root = tk.Tk()
root.title('TRACK SMART Attendence System')

#this to define canvas in GUI
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="lightgreen")
canvas.pack()

#to print welcome message
name_msg = tk.Message(canvas, text='WELCOME TO SMART TRACK ATTENDENCE SYSTEM')
name_msg.config(bg='lightgreen', font=('times', 24, 'italic'))
name_msg.place(relwidth=0.4, relheight=1)

#here i have added frame to our GUI for new user
frame = tk.Frame(root, bg='lightgreen', bd=10)
frame.place(relx=0.4, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

#button for new user
sign_up = tk.Button(frame, text="SIGN UP", font=40)
sign_up.place(relx=0.7, relheight=1, relwidth=0.3)


#creating lower frame for email entry
lower_frame = tk.Frame(root, bg='lightgreen', bd=10)
lower_frame.place(relx=0.4, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n')

#button for existing student
sign_in = tk.Button(lower_frame, text="SIGN IN", font=40)
sign_in.place(relx=0.7, relheight=1, relwidth=0.3)


root.mainloop()