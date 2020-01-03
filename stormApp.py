import os
import sys
import time
import datetime
import random
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import features
import wolframalph
import thunderstorm



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(input_text):
    # tts=gTTS(text=input_text,lang='en')
    # filename = 'voice.mp3'
    # tts.save(filename)
    # playsound.playsound(filename)
    engine.say(input_text)
    engine.runAndWait()

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        r.phrase_threshold = 0.2
        r.energy_threshold = 365
        audio= r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio,language='en-in')
            print("U said : " + said)

        except Exception as e :
            print("Exception: Sorry...I couldn't  recognize what u said "+str(e))
            (print('Say that again please ....'))
            speak('Could u please say that again ...')
            said= get_audio()
    return said

def wishMe():
    GREETING_INPUTS = ['hi' , 'hey' , 'wassup' , 'hello']
    GREETING_RESPONSES = ['hello' , 'hey there' ]
    HELP_GREET_RESPONSES = ['how may I help you' , 'I am now ready to take your commands' ,
                            'Please tell me what I can do for you']

    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <12 :
        speak('Good Morning Swarnit...')
        speak('I am Storm... Your Virtal Assistant')
        speak(features.getDate())
        speak(random.choice(HELP_GREET_RESPONSES))

    elif hour >=12 and hour <= 18 :
        speak('Good Afternoon Swarnit...')
        speak('I am Storm.... Your Virtal Assistant')
        speak(features.getDate())
        speak(features.getweather('Noida'))
        speak(random.choice(HELP_GREET_RESPONSES))

    else:
        speak('Good Night Sir..')
        speak('I am Storm... Your Virtal Assistant')
        speak(features.getDate())
        speak(random.choice(HELP_GREET_RESPONSES))

def wakeWord(text):
    WAKE_WORDS = ['hey storm' , 'okay storm' , 'hello storm']
    text = text.lower()
    for phrase in WAKE_WORDS :
        if phrase in text :
            return True

    return False

if __name__ =="__main__" :
    wishMe()
    print(features.getDate())
    while True :
        query = get_audio().lower()
        #query = 'open youtube for me'
        ### Logic based on query
        if 'wikipedia' in query:
            speak('searching that on wikipedia')
            query = query.replace("wikipedia", "")
            wiki_result = features.searchonWiki(query)
            speak("According to wikipedia  "+wiki_result)

        elif 'open google' in query :
            speak('Opening Google for you Sir')
            features.openGoogle()

        elif 'open youtube' in query :
            speak('opening Youtube for you Sir')
            features.openYoutube()

        elif 'search on google' in query :
            speak('Searching that on Google...')
            features.Googlesearch(query)

        elif 'tell me the weather' in query :
            speak('Of Which location Sir ?')
            city_name = get_audio()
            features.getweather(city_name)

        elif 'please quit' in query :
            speak('GoodBye Sir....'
                  'hope we meet soon..')
            sys.exit()

        elif 'activate alpha' in query :
            speak("Alpha mode activated")
            while True:
                speak(wolframalph.wolframalphafunc(query))
                query = get_audio().lower()
                if 'deactivate alpha' in query:
                    speak("Alpha mode deactivated...")
                    break
                else:
                    continue

        elif 'activate thunderstorm' in query :
            speak("Thunderstorm mode activated")
            while True:
                speak(thunderstorm.thunderstorm(query))
                query = get_audio().lower()
                if 'deactivate thunderstorm' in query:
                    speak("Thunderstorm mode deactivated...")
                    break
                else:
                    continue


