from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3
from os import path
import sys
import glob

"""VOICE"""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # object creation
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1


recognizer = sr.Recognizer()


'''Create file'''


def create_file():
    global recognizer

    engine.say("What do you want to write onto your file?")
    engine.runAndWait()

    done = False

    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio, language='en-in')
                note = note.lower()

                exist = False

                engine.say("choose a file name!")
                engine.runAndWait()

                while not exist:
                    try:

                        recognizer.adjust_for_ambient_noise(mic)
                        audio = recognizer.listen(mic)

                        file_name = recognizer.recognize_google(
                            audio, language='en-in')
                        file_name = file_name.lower() + '.txt'
                        file_present = path.exists(f"files/{file_name}")

                        if file_present == False:

                            with open(f"files/{file_name}", "w") as f:
                                f.write(note)
                                done = True
                                exist = True
                                engine.say(
                                    f"I succesfully created the file {file_name}")
                                engine.runAndWait()

                                # add file name to the database

                        else:
                            engine.say(
                                "Sorry file already exist!! Choose another file name.")
                            engine.runAndWait()

                    except sr.UnknownValueError:
                        recognizer = sr.Recognizer()
                        engine.say(
                            'I did not understant you! Please try again!')
                        engine.runAndWait()
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            engine.say(
                'I did not understant you! Please try again!')
            engine.runAndWait()


'''update file'''


def update_file():
    global recognizer

    engine.say('which action do you want to perform in the file.')
    engine.runAndWait()
    done = False

    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio, language='en-in')
                item = item.lower()

                done = True

                engine.say(f'I add {item} to the to do list!')
                engine.runAndWait()
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            engine.say('I did not understand. Please try again!')
            engine.runAndWait()


'''show file'''


def show_files():
    engine.say('The files on your directory are the following')
    engine.runAndWait()

    # fetch file_names from the database


'''greetings'''


def greetings():
    # print('hello')
    engine.say('Hello sir, what i can do for you?')
    engine.runAndWait()


'''exit'''


def quit():
    engine.say('See you soon, have a nice day!!')
    engine.runAndWait()
    sys.exit(0)


mappings = {
    'greeting': greetings,
    'create_file': create_file,
    'update_file': update_file,
    'show_files': show_files,
    'exit': quit
}


assistant = GenericAssistant(
    'data/intents.json', intent_methods=mappings)
# assistant.train_model()
# assistant.save_model(model_name="data/test_model")
assistant.load_model(model_name="data/test_model")

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic)
            print("Speak: ", end=" ")
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio, language='en-in')
            message = message.lower()

        assistant.request(message)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
