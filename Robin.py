from sys import maxunicode
from typing import Mapping
import pyttsx3 #pip install pyttsx3
import datetime 
import speech_recognition as sr  #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import pywhatkit
import pyautogui 
import requests
import time
import os
import smtplib
import random
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice' , voices[0].id)
print(voices[1].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon !")

    elif hour>=18 and hour<20:
        speak("Good Evening !")

    else:
        speak("Good Night , go get some rest now !")

speak("I am Robin at your service , please tell me how may i help you")

   

def takeCommand():
    # it takes mic input form the user and returns string output
   r = sr.Recognizer()
   with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
   try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

   except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
        
   return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('biswasvijay@gmail.com', 'your-password')
    server.sendmail('ambikbiswas7@gmail.com', to, content)
    server.close()


def instant_msgTo_Whatsapp(person_name , my_msg):
    webbrowser.open('https://web.whatsapp.com/')
    time.sleep(15)
    print(pyautogui.position())
    # click on search bar
    pyautogui.click(148,153)  #this ( x,y) co_ords can different for your computer
    pyautogui.typewrite(person_name)
    time.sleep(8)
    #click on person 
    pyautogui.click(165,271)#this ( x,y) co_ords can different for your computer
    time.sleep(5)
    pyautogui.typewrite(my_msg)
    time.sleep(3)
    pyautogui.press('Enter') # click on Send button
if __name__ == "__main__":
     wishMe()
    #  while True:
     if 1:
    #  takeCommand()
       query = takeCommand().lower()

       if 'wikipeia' in query:
            speak('searching wikipeida...')
            query = query.replace("wikipeida", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

       elif 'open youtube' in query:
          webbrowser.open("youtube.com")
 
        
       elif 'open google' in query:
          webbrowser.open("google.com")
        

       elif 'open facebook' in query:
         webbrowser.open("facebook.com")

       elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

       elif 'open word' in query:
            codepath="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.exe"
            os.startfile(codepath)
        
       elif 'open excel' in query:
            codepath="C:\\Program Files (x86)\Microsoft Office\\root\\Office16\\EXCEL.exe"
            os.startfile(codepath)

       elif 'open PowerPoint' in query:
            codepath="C:\\Program Files (x86)\Microsoft Office\\root\Office16\\POWERPNT.exe"
            os.startfile(codepath)


       elif 'open photoshop' in query:
            codepath="C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\photoshop.exe"
            os.startfile(codepath)
        
       elif 'play Video' in query:
            codepath="C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(codepath)
        
      
       elif 'play music' in query:
        music_dir = 'D:\\ mp3 Songs'
        song = os.listdir(music_dir)
        print(song)
     #    os.startfile(os.path.join(music_dir, song[0]))
        os.startfile(os.path.join(music_dir, random.choice(song)))

       elif 'the time' in query:
            strTime = datetime.datetime().now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

       elif 'open VS code' in query:
            codePath = "C:\\Users\\Laptop\AppData\Local\\Programs\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

       elif 'joke' in query:

            print(speak(pyjokes.get_joke()))

            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)



       elif 'whatsapp message' in query:

            try:
                speak("type the name below=>")
                person_name = input('Enter The Person Name Whom You Want To Send  Message: ')
                speak("now type your mesage")
                my_msg = input('Enter Your Message: ')
               
                instant_msgTo_Whatsapp(person_name=person_name,my_msg=my_msg)
                print("Your message is sending....")
                
            except Exception as e:
                print(e)
                speak("sorry , I am not able to send this whatsapp message")

       elif 'email to vijay' in query:
            try:
                    speak("what should i say..")
                    content = takeCommand()
                    to = "youremail01@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
            
            except Exception as e:
                   print(e)
                   speak("Sorry my friend Vijay. I am not able to send this email")   


       elif 'quit' in query:
        exit() 