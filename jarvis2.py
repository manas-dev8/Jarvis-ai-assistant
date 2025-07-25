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
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to cover voice into text
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
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Hello Sir, I am Jarvis. Please tell me how can I help you? ")

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("manassaxena9719@gmail.com", "manas8791299234")
    server.sendmail("manassaxena9719@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:
     if 1:

        query = takecommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            apath = "C:\\Windows\\notepad.exe"
            os.startfile(apath)

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe ")

        # closing k Liye .exe file ka location lagega.

        elif "open spotify" in query:
            speak("Yes sir, opening spotify for you")
            os.system("spotify.exe")

        elif "close spotify" in query:
            speak("Yes sir, Closing spotify now")
            os.system("taskkill /f /im spotify.exe")

        elif "open chrome" in query:
            bpath ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(bpath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            speak("Okay sir, closing command prompt")
            os.system("taskkill /f /im cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song[0]))

        elif "IP Address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=5)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")


        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open linkedin" in query:
            webbrowser.open("www.linkedin.com")

        elif "open microsoft" in query:
            webbrowser.open("www.microsoft.com")

        elif "Open OpenAI" in query:
            webbrowser.open("www.openai.com")

        elif "Open Boat" in query:
            webbrowser.open("www.boat.com")

        elif "open amazon" in query:
            webbrowser.open("www.amazon.com")

        elif "open flipkart" in query:
            webbrowser.open("www.flipkart.com")

        elif "Open Stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("Sir, What should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "Send Message" in query:
            kit.sendwhatmsg("+919548405463", "Hello Mitthu Bhai kya haL chal?",11,24)


        elif "play song on youtube" in query:
            speak("Which song you want to listen")
            ap = takecommand().lower()
            kit.playonyt(f"{ap}")


        elif "Send Email" in query:
            try:
                speak('What should i say?')
                content = takecommand().lower()
                to = "bhadwajshivang57@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to sahil")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this mail to sahil")

        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day.")
            sys.exit()

        speak("Sir, do you have any other work?")


