import pygame
import os
import datetime
import random
import psutil
import socket
import threading
import pyttsx3
from GoogleFeatures import googlecalenderfeatures, googlenewsfeatures, googleTranslate
from tkinter import *
from tkinter import simpledialog, Tk
from PIL import ImageTk, Image
import speech_recognition as sr
from AppFeatures import features, wolframalph
#thunderstorm

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def speak(audio):
    print('Storm:', audio)
    engine.say(audio)
    engine.runAndWait()


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.phrase_threshold = 0.290
        r.energy_threshold = 368
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio, language='en-in')
            print("U said : " + said)

        except Exception as e:
            print("Exception: Sorry...I couldn't  recognize what u said " + str(e))
            (print('Say that again please ....'))
            speak('Could u please say that again ...')
            said = myCommand()
    return said


def wake_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting to be called \
             Listening...")
        r.pause_threshold = 0.7
        r.phrase_threshold = 0.3
        r.energy_threshold = 375
        audio = r.listen(source)
        try:
            wake_cmd = r.recognize_google(audio, language='en-in')
            print("U said : " + wake_cmd)

        except Exception as e:
            wake_cmd = wake_command()
    return wake_cmd



