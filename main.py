import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text
import requests
from functions.os_ops import open_cmd, open_camera, open_chrome, open_visualstudiocode, open_visualstudio2019, openUnrealEngine
from functions.online_ops import trending_movies, play_on_yt, send_email,\
    send_whatsapp_message, search_google, search_on_wikipedia

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# set rate
engine.setProperty('rate', 200)

# set volume
engine.setProperty('volume', 1.0)

# set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_user():
    hour = datetime.now().hour
    if(hour >= 6) and (hour < 12):
        speak(f"Good morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USERNAME}")
    speak(f"I am {BOTNAME}. How can I help you?")


def user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising")
        query = r.recognize_google(audio, language="en-ke")

        if 'exit' not in query or 'stop' in query:
            speak(choice(opening_text))

        else:
            hour = datetime.now().hour
            if 21 <= hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
                exit()

    except Exception:
        speak("Sorry, didn't quite get that. Please repeat")
        query = 'None'

    return query


def main():
    greet_user()
    while True:
        query = user_input().lower()

        if 'open camera' in query:
            open_camera()
        elif 'youtube' in query:
            speak('What do you want to play on youtube sir?')
            video = user_input().lower()
            play_on_yt(video)
        elif 'open chrome' in query:
            open_chrome()
        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = user_input().capitalize()
            speak("What is the message sir?")
            message = user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")
        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*trending_movies(), sep='\n')
        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'visual studio code' in query:
            open_visualstudiocode()
        elif 'visual studio 2019' in query:
            open_visualstudio2019()
        elif 'Unreal Engine' in query:
            open_UnrealEngine()


if __name__ == "__main__":
    main()
