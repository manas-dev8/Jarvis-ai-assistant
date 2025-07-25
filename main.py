import win32com.client
import os

speaker= win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter the word you want to speak it out by computer")
    s = input()
    speaker.Speak(s)
def say(text):
    os.system(f'say{text}')
