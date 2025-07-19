#-----------------------------------------
# Voice Assistant Project using Python
# Name: Manjusree Valluri
# Description: This assistant listens to your voice, speaks responses,
#              tells the time, and plays YouTube videos.
# Date: July 2025
# -----------------------------------------


print("voice assistant is starting...")

import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        talk("Good morning!")
    elif hour < 18:
        talk("Good afternoon!")
    else:
        talk("Good evening!")
    talk("I am your assistant. How can I help you?")

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"You said: {command}")
            return command
    except:
        return ""

def run_assistant():
    greet()
    while True:
        command = take_command()

        if "time" in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The time is {current_time}")

        elif "play" in command:
            song = command.replace("play", "")
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif "stop" in command or "exit" in command or "bye" in command:
            talk("Goodbye! Have a nice day.")
            break

        elif command != "":
            talk("I did not understand. Please try again.")

# Start the assistant
run_assistant()


#libraries used:

#speech_recognition
#pyttsx3
#datetime
#pywhatkit

