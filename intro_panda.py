import os
import pandas as pd
from openpyxl import load_workbook
name = input("Enter your name - ")
df = pd.DataFrame({'Name' : [name]})
writer = pd.ExcelWriter('new.xlsx', engine='openpyxl')
writer.book = load_workbook('new.xlsx')
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
reader = pd.read_excel('new.xlsx')
df.to_excel(writer, index=False, header=False, startrow=len(reader)+1)
writer.close()

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "data/demo.xlsx"
path_local="new.xlsx";
storage.child(path_on_cloud).put(path_local)
#d = os.getcwd()
#os.chdir(d)
#storage.child(path_on_cloud).download("new.xlsx")

os.remove("new.xlsx")

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "data/demo.xlsx"
#path_local=r'D:\lol\demo.xlsx';
#storage.child(path_on_cloud).put(path_local)
#d = os.getcwd
#os.chdir(d)
storage.child(path_on_cloud).download("lol.xlsx")
