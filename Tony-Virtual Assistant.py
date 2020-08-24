# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:17:50 2020

@author: MAHESH.S.RACHHA
"""
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import datetime as dt
import wikipedia 
import webbrowser
import os
import smtplib

print("Initializing Tony..")


engine =pyttsx3.init('sapi5') #sapi5 is a driver of pyttsx3 module which help for intializing.. 
voices = engine.getProperty('voices') #gets all the properties of available voices.
engine.setProperty('voice',voices[0].id) #sets the the first audio from voices list.


# speak function will speak the given string..
def speak(text):    
    engine.say(text) #say fun speak the given text
    engine.runAndWait() #it will run and wait

    
def WishMe():
    hour = dt.datetime.now().hour#prints current minutes
    #print(hour)

    if(hour>=0 and hour<12):
        speak("Good morning Mahesh")
    
    elif(hour>=12 and hour<=16):
        speak("Good Afternoon Mahesh")
    
    else:
        speak("Good Evening Mahesh")
    
    speak("I am Tony,How may I help you ?")
    
#takecommand fun will take your command from your voice
def TakeCommand():
    m = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #audio = m.listen(source)
        audio = m.record(source,duration=3)
    try:
        print("Recognizing....")
        #print(m.recognize_google(audio),"\n")
    
        query = m.recognize_google(audio,language= 'en-in')
        print(f"user said :{query}\n")
        return query
        
    except Exception:          
        print("Sorry Say that again Please..")

speak("Intializing Tony...")
#speak("Hello Mahesh What can I do for you?")
WishMe()
query = TakeCommand()
query=query.lower()
#print(query)
    
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587) #smtp.gmail.com->smtp gmail server and 587 is port no..
    server.ehlo()
    server.starttls()
    server.login("etribewebsite@gmail.com","etribeweb")
    server.sendmail("jagdishrj90@gmail.com",to,content)
    server.close
    
#logic for executing the tasks as per the query
def main():
    global query
    
    if('who' in query):
        speak("Searching Wikipedia...")
        #query = query.replace('wikipedia','')
        results=wikipedia.summary(query,sentences=2)
        speak(results)
    
    elif('wikipedia' in query):
        speak("Searching Wikipedia...")
        query = query.replace('wikipedia','')
        results=wikipedia.summary(query,sentences=2)
        speak(results)
    
    elif('youtube' in query):
        speak("Starting Youtube...")
        url="youtube.com"
        
        chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chromepath).open(url)   
 
    elif('google' in query):
        speak("starting Google...")
        url="google.com"
        chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chromepath).open(url)

    elif('gmail' in query):
        speak("starting Gmail...")
        url="https://mail.google.com/mail/u/0/#inbox"
        chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chromepath).open(url)
    
    elif('gst' in query):
        speak("starting GST...")
        url="https://services.gst.gov.in/services/login"
        chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chromepath).open(url)
    
    elif('play music' in query):
        speak("Playing Music...")
        songs=os.listdir("C:\\Users\\MAHESH.S.RACHHA\\Music")
        print(songs)
        os.startfile(os.path.join("C:\\Users\\MAHESH.S.RACHHA\\Music",songs[2]))
    
    elif('time' in query):
        #speak("Playing Music...")
        time=dt.datetime.now().strftime("%H:%M:%S")
        speak("Hey Mahesh,the current time is "+time)
        
    elif('notepad' in query):
        speak("Opening Notepad...")
        os.startfile("C:\Windows\System32\\notepad.exe")
        
    elif('notepad' in query):
        speak("Opening Notepad...")
        os.startfile("C:\Windows\System32\\notepad.exe")
        
    
    elif('email' in query):
        try:
            speak("What should I send")
            content =TakeCommand()
            to = "jagdishrj90@gmail.com"
            sendmail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print("sorry something gone wrong")
main()