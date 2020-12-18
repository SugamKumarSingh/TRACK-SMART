import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
with mic as source:
  r.adjust_for_ambient_noise(source, duration=1)
  print("What is your name: ")
  audio = r.listen(source, timeout=7)
  print("Wait till your voice is recognised......\n")
try:
  print("You are entering as " + r.recognize_google(audio) + "?")
  val = input("Yes or No?\n")
  if val == "yes" and "YES" and "Yes" : 
    print("You are entering as " + r.recognize_google(audio)+ ".")
except:
  print("Unable to Understand,Please try it once again")