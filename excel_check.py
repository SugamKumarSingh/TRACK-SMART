import smtplib 
import pandas as pd
import numpy as np
import os

d=r'D:\lol'
os.chdir(d)

df = pd.read_excel('demo.xlsx')

name=input("Enter your name - ")

x=[]

x=df[df['Name']==name]['email'].tolist()
print(x[0])


