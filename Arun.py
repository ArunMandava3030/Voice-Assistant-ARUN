import pyttsx3 #pip install pyttsx3
import requests
import json 
import speech_recognition as sr#pip install speechRecognition
import datetime
import wikipedia#pip install wikipedia
import webbrowser
import os
from  bs4 import BeautifulSoup
import smtplib


from wikipedia.wikipedia import search, summary

print("initializing Arun")

MASTER="Arun"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

#speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function will wish you as per the current time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!!"+MASTER)

    elif hour>=12 and hour<17:
        speak("Good Afternoon"+MASTER)

    else:
        speak("Good Evening!!"+MASTER)


    #speak("i am Arun how can i help you")

#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        audio= r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        print("i didn't get you SIR!!!")
        query=None
    return query


def sendEmail(to, content):
    server=smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo
    server.starttls()
    server.login('yourgmail@gamil.com','password')
    server.sendmail('reseveremailid',to,content)
    server.close()

def Temp():
      search ="temperature in poranki"
      url=f"https://www.google.com/search?q={search}"
      r= requests.get(url)
      data = BeautifulSoup(r.text,"html.parser")
      temperature = data.find("div", class_ ="BNeawe").text
      speak(f"temperature in poranki is {temperature} ")


#main program starts here...
if __name__=="__main__":
    wishMe()
    while True:
     query=takeCommand()
     
     if 'wikipedia' in query.lower():
         speak('searching wikipedia')
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         speak("acoordind to wikipedia")
         print(results)
         speak(results)

     elif'open youtube' in query.lower():
         webbrowser.open("youtube.com")

     elif'open google' in query.lower():
         webbrowser.open("google.com")

     elif'open stack overflow' in query.lower():
         webbrowser.open("stackoverflow.com")

     elif'open github' in query.lower():
         webbrowser.open("github.com")
     elif'temperature' in query:
         Temp()
     elif 'play music'in query.lower():
         music_dir="C:\\Users\\arunm\\Desktop\\Songs"
         songs=os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir,songs[0]))
    
     elif'the time'in query:
         strTime=datetime.datetime.now().strftime("%H:%M:%S")
         print(strTime)
         speak(f" Sir, the time is {strTime}")
    
     elif'open code' in query:
         codepath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codepath)
        

     elif'email to arun' in query:
        try:
             speak("what should i do")
             content=takeCommand
             to="arunmandava3030@gmail.com"
             sendEmail(to, content)
             speak("Email has been sent!!")
        except Exception as e:
            print(e)
            speak("Sorry sir .I couldn't sent a mail to this email")

     if  'go to sleep' in query:
         exit()


        









   
