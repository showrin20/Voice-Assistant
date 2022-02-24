import pyttsx3
import pywhatkit
import datetime
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pyjokes
import os
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning shona!  I love you")

    elif hour>=12 and hour<18:
        speak("Good Afternoon shona! I love you")   

    else:
        speak("Good Evening shona! I love you") 
def video():
    try:
        pywhatkit.playonyt("dhakar pola")
        print("Playing...")
 
    except:
        print("Network Error Occured") 
def loveletter():
    try:
        pywhatkit.sendwhatmsg("+8801841124930", "Dear I am so glad to inform u that I have fallen in love with you since the first day I met you. I would like to present myself as a prospective lover. Our love affair would be on probation for a period of two months. Upon completion of probation, there will be performance appraisal leading to promotion from lover to spouse.",0, 0)
        print("sent it love!")
    except:
        print("An Unexpected Error!")
def find():
    try:
        pywhatkit.search("Matrimony")
        print("Searching...")
 
    except:
       print("An unknown error occured")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:   
        print("Say that again please...") 
        return "None" 
    return query
speak("Hello I am dhakar pola. Your voice is my favorite sound, your name is my favorite word, and your hug is my favorite place to be.")
if __name__=="__main__" :
    wishme()
    while True:   
        query = takeCommand().lower()
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open tinder' in query:
            webbrowser.open("tinder.com")
        elif 'joke' in query:
            joke_1=pyjokes.get_joke()
            speak(joke_1)
            print(joke_1)
        elif 'romantic' in query:
            video()
        elif 'love' in query:
            loveletter()
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'search' in query:
            topic = query.replace('search', '')
            speak('searching ' + topic)
            pywhatkit.search(topic)
        elif 'find' in query:
            find()
            
        elif 'date' in query:
            speak('I knew today was going to be a good day, I read it in my morning tea leaves.')
        else:
            speak('Shona,How can I make you feel special')









if __name__=="__main__" :
    speak()

    
