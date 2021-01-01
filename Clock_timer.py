##import library
from tkinter import *
import time
from playsound import playsound
#from PIL import Image,ImageTk
import os
#background image
#image = Image.open("COUNT.jpg")
#photo = ImageTk.PhotoImage(image)

#wlcmLabel = tk.Label(image=photo)
#wlcmLabel.pack()


## display window 
root = Tk()
root.geometry('800x500')
root.resizable(0,0)
root.config(bg ='blanched almond')
root.title('Countdown')
Label(root, text = 'TRY AFTER  REMANING TIME ' , font = 'Algerian 30 bold', fg='RED', bg ='BLACK').pack()


##########fun to start countdown

def countdown():
    times = 300
    while times > -1:
        minute,second = (times // 60 , times % 60)


        Label(root, font ='ALGERIAN 100 bold', text = '%i:%i'%(minute,second),   bg ='papaya whip').place(x = 270 ,y = 200)
        root.update()
        time.sleep(1)

        if(times == 0):
            playsound('Loud_Alarm_Clock_Buzzer.mp3')
            Button(root, text='RETRY', bd ='5', command = '', bg = '#ff6300', font = 'InkFree 10 bold').place(x=60, y=400)
        times -= 1

Button(root, text='START', bd ='5', command = countdown, bg = 'antique white', font = 'arial 10 bold').place(x=150, y=350)
Button(root, text='RETRY', bd ='5', command = '', bg = '#ff6200', font = 'InkFree 10 bold',state=DISABLED).place(x=60, y=400)
Button(root, text='CANCEL', bd ='5', command = '', bg = '#ff6200', font = 'InkFree 10 bold').place(x=600, y=400)

root.mainloop()




