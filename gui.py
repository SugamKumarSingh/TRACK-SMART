import tkinter as tk

HEIGHT = 500
WIDTH = 700

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
frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

#entry field for name
name = tk.Entry(frame, font=40)
name.place(relwidth=0.65, relheight=1)

#button for name
name_button = tk.Button(frame, text="SUBMIT Name", font=40)
name_button.place(relx=0.7, relheight=1, relwidth=0.3)


#creating lower frame for email entry
lower_frame = tk.Frame(root, bg='lightyellow', bd=10)
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n')

#entry field for email
email = tk.Entry(lower_frame, font=40)
email.place(relwidth=0.65, relheight=1)

#button for email
email_button = tk.Button(lower_frame, text="SUBMIT Email", font=40)
email_button.place(relx=0.7, relheight=1, relwidth=0.3)


root.mainloop()