import smtplib 
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
x = excel_data_df['P/A'].tolist()
name = input("Enter your name - ")
#x.append(' ')
i=0
p=0
a=0
for i in x:
   if(i==name):
      for j in y:
          if(j=="Present")
             p=p+1
      break;
    
os.remove("new.xlsx")

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
if(p==1):
  s.sendmail("tracksmartattendance@gmail.com", "ENTER YOU EMAIL HERE", message) 
else:
  s.sendmail("tracksmartattendance@gmail.com", "ENTER YOU EMAIL HERE", message1) 
 
  
# terminating the session 
s.quit() 
