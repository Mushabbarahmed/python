from tkinter import *

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from  pygame import mixer
import re
def ms(s1,stopper):
    # print("music")
    mixer.init()
    mixer.music.load(s1)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am . Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.energy_threshold
        #r.pause_threshold = 1
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


def alarm():
    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.play()

    while True:
        a=takeCommand()
        #a = input("enter if you want to stop")
        if a == "stop":
            mixer.music.stop()
            break
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    wishMe()
    #takeCommand()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        # if 'wikipedia' in query:
        #     speak('Searching Wikipedia...')
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)

        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'alarm' in query:
            # strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # speak(f"The current time is {strTime}")
            try:
                path = re.compile(r'\d{2}:\d{2}')
                matches = path.finditer(query)
                for match in matches:
                    print(" ")
                h = str(match)
                time1 = h[40:45]
                # print(time1)
            except Exception as e:
                path = re.compile(r'\d{1}:\d{2}')
                matches = path.finditer(query)
                for match in matches:
                    print(" ")
                h = str(match)
                time1 = h[40:44]
                # print(time1)
            finally:
                if "p.m" in query:
                    ti = int(time1.split(":")[0]) + 12
                    tim = str(ti)
                    time2 = tim + ":" + time1.split(":")[1] + ":00"
                    print(time2)
                else:
                    time2 = "0" + time1 + ":00"
                    print(time2)


                def alarm():

                    mixer.init()
                    mixer.music.load("eyes.mp3")
                    mixer.music.play()

                    while True:
                        a=takeCommand()
                        print("enter if you want to stop")
                        if a == "stop":
                            mixer.music.stop()
                            break
                        # snooze()


            while True:

                time = datetime.datetime.now().strftime("%H:%M:%S")
                # print(time)
                if time2 == time:
                    alarm()
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'hashim' in query:

            ms("good3.mp3","stop")
        elif 'muzaffar' in query:

            ms("good5.mp3","stop")
        elif 'noman' in query:

            ms("good7.mp3","stop")
        elif 'hana' in query:

            ms("good4.mp3","stop")
        elif 'faizan' in query:

            ms("good6.mp3","stop")
        elif 'farhan' in query:

            ms("good8.mp3","stop")
        elif 'kaif' in query:

            ms("good9.mp3","stop")
        # elif 'open stackoverflow' in query:
        #     webbrowser.open("stackoverflow.com")
        #
        #
        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'email to harry' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "harryyourEmail@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend harry bhai. I am not able to send this email")
