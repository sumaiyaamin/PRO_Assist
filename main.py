import pyttsx3 #pip install pyttsx3
import speech_recognition as speech #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pywhatkit #pip install pywhatkit
import pyjokes


eng = pyttsx3.init('sapi5') 
voice = eng.getProperty('voices') 
# eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
eng.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
eng.runAndWait()

#Speak Function 
def speak(text):
    eng.say(text)
    eng.runAndWait()

string1 = ["\t\tInitializing PRO"]

from time import sleep
import sys

for string in string1:          
    for c in string:          
        print(c, end='')    
        sys.stdout.flush() 
        sleep(0.08)          
    print('') 
speak("Initializing PRO...")
name =input("Enter your name : ")

def wish():
    hour = int(datetime.datetime.now().hour)   

    if hour>=0 and hour<12:
        speak(f"Good Morning...{name}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon..{name}")
    else:
        speak(f"Good Evening...{name}")

wish()  
speak("I am PRO. How may I help you?") 

#take command from microphone
def command():
    r = speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...") #pip install PyAudio
        audio = r.listen(source)
        

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language ='en-US') 
        query = query.lower()
        if 'pro' in query :
                query = query.replace('pro', '')
                
                speak(query) 
        
    except Exception as e:
        print("Oops! Say that again please...")
        query = None
    return query


#main program
def run_pro():   
    query = command()
    if 'play' in query:
            song = query.replace('play'," ")
            speak("playing..." + song)
            pywhatkit.playonyt(song)
    elif 'open youtube' in query.lower():

        url = "youtube.com"
        chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    elif 'open google' in query.lower():

        url = "google.com"
        chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        
    elif 'open facebook' in query.lower():

        url = "facebook.com"
        chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"{name} The time is {strTime}")
    elif 'messenger' in query.lower():
        codepath = r"C:\Users\HP\AppData\Local\Programs\Messenger\Messenger.exe"
        os.startfile(codepath)
    elif 'code blocks' in query.lower():
        codepath1= "C:\Program Files\CodeBlocks\codeblocks.exe"
        os.startfile(codepath1)
    elif 'zoom' in query.lower():
        codepath2= r"C:\Users\HP\AppData\Roaming\Zoom\\bin\Zoom.exe"
        os.startfile(codepath2)
    elif 'who is ' in query:
            person = query.replace('who is ', " ")
            info = wikipedia.summary(person, sentences=5)
            print(info)
            speak(info)
    elif 'what is ' in query:
            thing = query.replace('what is ', " ")
            result = wikipedia.summary(thing, sentences=5)
            print(result)
            speak()
    elif 'joke' in query :
            speak(pyjokes.get_joke())

while True:
    run_pro()

