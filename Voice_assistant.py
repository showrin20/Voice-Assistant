# Install required libraries before running the script
# pip install pyttsx3
# pip install pywhatkit
# pip install SpeechRecognition
# pip install googletrans==4.0.0-rc1
# pip install gtts
# pip install pyjokes
# pip install wikipedia
# pip install pyaudio (For SpeechRecognition, may require manual installation)

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

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Speak the provided text."""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning shona! I love you")
    elif 12 <= hour < 18:
        speak("Good Afternoon shona! I love you")
    else:
        speak("Good Evening shona! I love you")

def video():
    """Play a specific video on YouTube."""
    try:
        pywhatkit.playonyt("dhakar pola")
        print("Playing...")
    except:
        print("Network Error Occurred")

def loveletter():
    """Send a love message via WhatsApp."""
    try:
        pywhatkit.sendwhatmsg("+8801841124930", 
                              "Dear I am so glad to inform you that I have fallen in love with you since the first day I met you. "
                              "I would like to present myself as a prospective lover. Our love affair would be on probation for a period of two months. "
                              "Upon completion of probation, there will be a performance appraisal leading to promotion from lover to spouse.", 
                              datetime.datetime.now().hour, 
                              datetime.datetime.now().minute + 1)
        print("Love message sent!")
    except:
        print("An Unexpected Error!")

def find():
    """Search for matrimony online."""
    try:
        pywhatkit.search("Matrimony")
        print("Searching...")
    except:
        print("An unknown error occurred")

def takeCommand():
    """Take microphone input and return the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query

# Initial greeting
speak("Hello, I am Dhakar Pola. Your voice is my favorite sound, your name is my favorite word, and your hug is my favorite place to be.")

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, no information was found on this topic.")
        elif 'open tinder' in query:
            webbrowser.open("https://tinder.com")
        elif 'joke' in query:
            joke_1 = pyjokes.get_joke()
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
            speak('Shona, how can I make you feel special')
