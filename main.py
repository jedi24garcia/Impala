#!/usr/bin/env python3

import speech_recognition as sr
from AppKit import NSSpeechSynthesizer
from Foundation import NSSpeechSynthesizer, NSArray

def getVoice():
  voices = NSSpeechSynthesizer.availableVoices()
  voicenames = []
 
  for voice in voices:
    voiceattr = NSSpeechSynthesizer.attributesForVoice_(voice)
    voicename = voiceattr['VoiceName']
    if voicename not in voicenames:
      voicenames.append(voicename)
  return voicenames

def speak(text, voicename):
  synthesizer = NSSpeechSynthesizer.alloc().initWithVoice_(voicename)
  if synthesizer:
    synthesizer.startSpeakingString_(text)
  else:
    print(f"Voice '{voicename}' is not available.")

if __name__ == '__main__':
  voicenames = getVoice()
  if not voicenames:
    print("Unavailable")
  else:
    for voicename in voicenames:
      print(voicename) 

      selected_persona = voicenames[0]
      text_to_speak = "Hello"

      speak(text_to_speak, selected_persona)
