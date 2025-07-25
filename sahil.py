import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
#for voice in voices:
   #engine.setProperty('voice',voice.id)
    #engine.say("hello sir friday this side")
#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please")
        return "none"
    return query

def wish():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good evening")
    else:
        speak("good evening")
    speak("I am FRIDAY sir. please tell me how can i help you ")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',535)
    server.ehlo()
    server.starttls()
    server.login('ms9811151061@gmail.com', 'mohd8sahil@')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:
     if 1:

        query = takecommand().lower()

        #logic building for tasks

        if 'open chrome' in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(npath)

        elif 'open notepad' in query:
            spath = "C:\Windows\notepad.exe"
            os.startfile(spath)

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
                cap.release()
                cv2.destroyAllWindows()
        elif 'play music' in query:
            music_dir = "D:\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                   os.startfile(os.path.join(music_dir, songs[0]))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
           #print(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open discord" in query:
            webbrowser.open("www.discord.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")

        elif "open something" in query:
            webbrowser.open("https://aniwatch.to/tv")

        elif "send message" in query:
            speak("for whome sir you want send msg?")
            no = takecommand()
            kit.sendwhatmsg(f"{no}", "this is testing protocol",20,15)

        elif "play song on youtube" in query:
            speak("which song you want to listen")
            ap = takecommand().lower()
            kit.playonyt(f"{ap}")

        elif "send email to sahil" in query:
            try:
                speak("what should i say")
                content = takecommand().lower()
                to = "sahil10avengers@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to sahil")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this email to sahil")