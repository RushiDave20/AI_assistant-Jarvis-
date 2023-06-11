from email.mime import audio
from importlib.util import set_loader
from unittest import result
import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

   
    except Exception as e:


        # print(e)    
        print("Say that again please...")  
        return "None"
    return query





def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
        

    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir")
        
    else:
        speak("Good Evening Sir")

    speak("I am Jarvis Sir, How may I help you?")
    
 

if __name__ == "__main__":
    wishMe()
  
    while True:
         query = takeCommand().lower()
        
        #Logic for executing task based on query
        
         if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
         elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
         elif 'open google' in query:
            webbrowser.open("google.com") 
            
         elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            
         elif 'open amazon' in query:
            webbrowser.open("amazon.com")
            
         elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
        
         elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
            
         elif 'play music' in query:
            music = "E:\MUSIC"
            songs = os.listdir(music)
            print(songs)    
            os.startfile(os.path.join(music, songs[0]))
            
         elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        
                      
         elif 'thank you' in query:
             speak("No problem sir")
            
         elif 'good bye' in query:
             speak("Good bye sir")
            
         elif 'good night' in query:
             speak("Good night sir.")
             
         elif 'good afternoon' in query:
             speak("Good afternoon sir.")
             
        
         elif 'good morning' in query:
             speak("Good morning sir,have a great day!")
                  
         elif 'good evening' in query:
             speak("Good evening sir,how is your day?")
         
         elif 'it is good' in query:
             speak("That is good to hear sir!")
             
         
         elif 'how are you' in query:
             speak("I am fine sir!,What about you?")
             
         
         elif 'i am good' in query:
             speak("That is good to hear sir!")
             
         elif 'i love you' in query:
             speak("i love you too sir!")
        
         elif 'play games' in query:
            games = "D:\\Games\\Forza Horizon 5"
            gaming = os.listdir(games)
            print(gaming)    
            os.startfile(os.path.join(games, gaming[13]))
            
         elif 'what i am supposed to do' in query:
             speak("Sir,You should have a cup of tea,And have a biscut, too")
           
         elif 'it is evening' in query:
             speak("Sir! you have to  have dinner as soon as possible.")
    
         elif 'happy diwali' in query:
             speak("Happy diwali you too sir!,May the mithai, rangoli and diyas make your day sweet,colorful and bright!")
        
