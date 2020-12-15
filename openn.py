from tkinter import Tk     
from tkinter.filedialog import askopenfilename
from PIL import Image 
Tk().withdraw() 
filename = askopenfilename()
print(filename)
im = Image.open(filename)  
im.show()  
