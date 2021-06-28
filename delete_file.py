from voice_recognizer import *
from os import path, remove
import db_connect

'''Delete files'''


def delete_files(username):
    global recognizer

    engine.say('Which file do you want to delete?')
    engine.runAndWait()
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.pause_threshold = 0.6
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)

                file_name = recognizer.recognize_google(
                    audio, language='en-in')
                file_name = file_name.lower()
                print(file_name)

                file_present = path.exists(f"files/{username}/{file_name}.txt")

                if file_present == True:

                    remove(f"files/{username}/{file_name}.txt")

                    engine.say(
                        f'I successfully deleted {file_name}.txt to from the directory!')
                    engine.runAndWait()

                    done = True
                else:
                    print("Bot: Sorry file not found!! Choose another file name.")
                    engine.say(
                        "Sorry file not found!! Choose another file name.")
                    engine.runAndWait()

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            engine.say('I did not understand. Please try again!')
            engine.runAndWait()
