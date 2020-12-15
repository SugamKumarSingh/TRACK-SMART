  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
  
# start TLS for security 
#s.starttls() 
  
# Authentication 
s.login("tracksmartattendance@gmail.com", "12345678a@") 
  
# message to be sent 
message = "Hi!!!"
  
# sending the mail 
s.sendmail("tracksmartattendance@gmail.com", "ENTER YOU EMAIL HERE", message) 
  
# terminating the session 
s.quit() 
