import os
import speech_recognition as sp
import pyttsx3

pyttsx3.speak("Welcome to my MLOPS program")

pyttsx3.speak("What can i do for you, you can call me zeus")


r = sp.Recognizer()
with sp.Microphone() as source:
    print("Wait for speach")
    output = r.listen(source)
    print("done")

data = r.recognize_google(output)

print(data)

if "Notepad" in data:
  os.system("notepad")
elif "Chrome" in data:
  os.system("start chrome")
else:
  pyttsx3.speak("are you aware of windows command") 


