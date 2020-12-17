import pyrebase
import os
import pandas as pd
from openpyxl import load_workbook
def su_name():
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

    path_on_cloud = "data/excel/sheett.xlsx"
    d = os.getcwd()
    os.chdir(d)
    storage.child(path_on_cloud).download("temp.xlsx")

    excel_data_df = pd.read_excel('new.xlsx')
    x=[' ']
    #df# print whole sheet data
    x = excel_data_df['Name'].tolist()
    #x.append(' ')
    i=0
    p=0
    a=0
    for i in x:
       if(i==name):
          p=p+1
          break;

    if(p==0):
        df = pd.DataFrame({'Name' : [name]})
        writer = pd.ExcelWriter('temp.xlsx', engine='openpyxl')
        writer.book = load_workbook('temp.xlsx')
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        reader = pd.read_excel('temp.xlsx')
        df.to_excel(writer, index=False, header=False, startrow=len(reader)+1)
        writer.close()

        path_local="new.xlsx"
        storage.child(path_on_cloud).put(path_local)

        os.remove('temp.xlsx')

    else:
        print("Your name is already on the list, SIGN IN")
