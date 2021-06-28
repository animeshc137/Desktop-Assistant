import speech_recognition as sr
import pyttsx3

"""VOICE"""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # object creation
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1


recognizer = sr.Recognizer()
