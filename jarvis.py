from http import server
from importlib.resources import path
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("good mornning!")
        elif hour>=12 and hour<18:
                speak("good afternoon !")
        else:
                speak("good evening!")
        speak("how may i help you !")
         
def   Takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
         
    except Exception as e:
        print(e)

        print("say that again please..")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pankajrawat3214@gmail.com','garhwali')
    server.sendmail('pankajrawat3214@gmail.com',to, content)
    server.close( )
if __name__ == "__main__":
    speak("hello your personal assistance here")
    wishMe()
     

    # while True:
    if 1:
        query = Takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to the wikipedia...")
            print(results)
        
            speak(results )  
 
        elif'open youtube' in query:
            webbrowser.open("youtube.com")

        elif'open google' in query:
            webbrowser.open("google.com")

        elif'open microsoft' in query:
            webbrowser.open("microsoft.com")

        elif'open whatsapp' in query:
            webbrowser.open("whatsapp.com")


        elif 'play music' in query:
            music_dir = 'c:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[4]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif'open chrome' in query:
           Chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
           os.startfile(Chromepath)
        
        elif 'email to akansha' in query:
            try:
                speak("what should i say?")
                content = Takecommand()
                to = "akansha.rawat@themathcompany.com"
                sendEmail(to,content)
                speak("email has sent!")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send this email")
            



    