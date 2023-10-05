#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak():
  engine.say(text)
  engine.runAndWait()
  engine.stop()


speak("hello")
