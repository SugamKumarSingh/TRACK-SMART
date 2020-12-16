import tkinter as tk

HEIGHT = 500
WIDTH = 700

root = tk.Tk()
root.title('TRACK SMART Attendence System')

#this to define canvas in GUI
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="lightgreen")
canvas.pack()


#upper frame for heading
upper_frame = tk.Frame(root, bg='lightgreen', bd=10)
upper_frame.place(relx=0.5, relwidth=1, relheight=0.3, anchor='n')

#to print welcome message
name_msg = tk.Message(upper_frame, text='WELCOME TO SMART TRACK ATTENDENCE SYSTEM')
name_msg.config(bg='lightgreen', font=('times', 24, 'italic'))
name_msg.place(relwidth=1, relheight=1)


#here i have added frame to our GUI for new user
frame = tk.Frame(root, bg='lightgreen', bd=10)
frame.place(relx=0.75, rely=0.4, relwidth=0.75, relheight=0.1, anchor='n')

#button for new user
sign_up = tk.Button(frame, text="SIGN UP", font=40)
sign_up.place(relheight=1, relwidth=0.3)


#creating lower frame for email entry
lower_frame = tk.Frame(root, bg='lightgreen', bd=10)
lower_frame.place(relx=0.75, rely=0.6, relwidth=0.75, relheight=0.1, anchor='n')

#button for existing student
sign_in = tk.Button(lower_frame, text="SIGN IN", font=40)
sign_in.place(relheight=1, relwidth=0.3)


root.mainloop()