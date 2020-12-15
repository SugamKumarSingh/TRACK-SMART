import pandas as pd
import numpy as np
import pyrebase
import os
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
path_on_cloud = "data/demo.xlsx"
#path_local=r'D:\lol\demo.xlsx';
#storage.child(path_on_cloud).put(path_local)
d = os.getcwd()
os.chdir(d)
storage.child(path_on_cloud).download("new.xlsx")


excel_data_df = pd.read_excel('new.xlsx')
x=[' ']
#df# print whole sheet data
x = excel_data_df['Name'].tolist()
name = input("Enter your name - ")
#x.append(' ')
i=0
p=0
a=0
for i in x:
   if(i==name):
      p=p+1
      break;
  

os.remove("new.xlsx")
if(p==1):
  print("Your name is in our records")
else:
  print("Your name is not in our records")
    
