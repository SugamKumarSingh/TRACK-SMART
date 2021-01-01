import tkinter as tk
from PIL import Image, ImageTk

HEIGHT = 2048
WIDTH = 2048
bgc='lightyellow'

root = tk.Tk()
root.title('TRACK SMART Attendence System')

#this to define canvas in GUI
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

btn_image = Image.open("black_bioChem.jpeg")
btn_photo = ImageTk.PhotoImage(btn_image)

vrPasscode = tk.Button(canvas, image = btn_photo, font=('times', 36))
vrPasscode.place(relx=0.32, rely=0.2, relwidth=0.36, relheight=0.6)

root.mainloop()