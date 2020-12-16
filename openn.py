from tkinter import Tk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import pyrebase
import os
def openn():
    Tk().withdraw() 
    filename = askopenfilename()
    config = {
          "apiKey": "AIzaSyAXtE0fQeJSN8r1Omtyx5vTlsdyYrF9XpE",
        "authDomain": "tympass-32736.firebaseapp.com",
        "databaseURL" : "https://tympass-32736.firebaseio.com",
        "projectId": "tympass-32736",
        "storageBucket": "tympass-32736.appspot.com",
        "messagingSenderId": "990276104410",
        "appId": "1:990276104410:web:a6d956ded09fc3c958b5e3",
        "measurementId": "G-7HF9TQ5QC1"
        }
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage() 

    path_on_cloud = ("data/images/"+str(name)+".jpg")
    path_local=(filename);
    storage.child(path_on_cloud).put(path_local)
 

