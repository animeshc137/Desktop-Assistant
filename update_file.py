from voice_recognizer import *
from os import path, remove, rename
import db_connect

# '''update file (Animesh)'''


# def update_file(username):

#     global recognizer

#     engine.say("""Which action do you want to perform in the file.
#                 You can Clear everything and start fresh
#                 Append to the file.
#                 Replace a certain word with a new word
#                 Or You can delete the file entirely""")

#     engine.runAndWait()

#     done = False
#     while not done:
#         try:
#             with sr.Microphone() as mic:
#                 recognizer.pause_threshold = 0.6
#                 recognizer.adjust_for_ambient_noise(mic)
#                 audio = recognizer.listen(mic)
#                 item = recognizer.recognize_google(audio, language='en-in')
#                 item = item.lower()
#                 print(item)
#         except sr.UnknownValueError:
#             recognizer = sr.Recognizer()
#             print(
#                 'Bot: I did not understant you! Please try again!')
#             engine.say(
#                 'I did not understant you! Please try again!')
#             engine.runAndWait()


# username = "abhinav19"
# update_file(username)
