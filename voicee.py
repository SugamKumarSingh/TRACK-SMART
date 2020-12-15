# Import the required module for text  
# to speech conversion 
from gtts import gTTS

  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = input("Enter your name - ")
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text="Your name has been saved as" + str(mytext), lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome
d=os.getcwd()
os.chdir(d)
myobj.save("welcome.mp3") 

# Playing the converted file
#welcome = r'D:\voce\welcome.mp3'
#os.system("mpg123" + welcome) 

from playsound import playsound
playsound("welcome.mp3")

os.remove("welcome.mp3")


