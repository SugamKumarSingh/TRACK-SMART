import smtplib 
import pandas as pd
import numpy as np
import pyrebase
import os
'''config = {
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
storage.child(path_on_cloud).download("new.xlsx")'''

d=r'D:\lol'
os.chdir(d)

df = pd.read_excel('demo.xlsx')



name=input("Enter your name - ")

x=[]

x=df[df['Name']==name]['email'].tolist()
k=x[0]
print(k)

y=[]

y=df[df['Name']==name]['P/A'].tolist()
j=y[0]

p=0

if(j=='Present'):
   p=p+1
      
      
    
#os.remove("demo.xlsx")

# creates SMTP session 
s = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
  
# start TLS for security 
#s.starttls() 
  
# Authentication 
s.login("tracksmartattendance@gmail.com", "12345678a@") 
  
# message to be sent 
message = "You have been marked as present today."
message1 = "You have been marked as absent today." 
  
# sending the mail
print(p)

if(p==1):
   s.sendmail("tracksmartattendance@gmail.com", k, message) 
else:
   s.sendmail("tracksmartattendance@gmail.com", k, message1) 
 
  
# terminating the session 
s.quit() 
