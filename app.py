from neuralintents import GenericAssistant
from voice_recognizer import *
from datetime import *
from os import system, path
import sys
import db_connect
import weather
import news
import create_file
import update_file
import show_files
import delete_file

user_name = 'default'


'''greetings'''


def greetings():
    engine.say(f'Hello {user_name}, what I can do for you?')
    engine.runAndWait()


'''exit'''


def quit():

    print('Bot: See you soon, have a nice day!!')
    engine.say('See you soon, have a nice day!!')
    engine.runAndWait()
    sys.exit(0)


def create():
    create_file.create_file(user_name)


def update():
    update_file.update_file(user_name)


def show():
    show_files.show_files(user_name)


def delete():
    delete_file.delete_files(user_name)


def weather():
    weather.weather_report()


def news():
    news.news_report()


mappings = {
    'greeting': greetings,
    'create_file': create,
    'update_file': update,
    'show_files': show,
    'delete_files': delete,
    'weather_report': weather,
    'news_report': news,
    'exit': quit
}


def my_assistant(username):
    global recognizer
    global user_name

    user_name = username

    engine.say(f'Hello {user_name}, what I can do for you?')
    engine.runAndWait()

    # assistant = GenericAssistant(
    #     'data/intents.json', intent_methods=mappings)
    # # assistant.train_model()
    # # assistant.save_model(model_name="data/test_model")
    # assistant.load_model(model_name="data/test_model")

    # while True:
    #     try:
    #         with sr.Microphone() as mic:
    #             recognizer.pause_threshold = 0.6
    #             recognizer.adjust_for_ambient_noise(mic)
    #             print("Speak: ")
    #             audio = recognizer.listen(mic)

    #             message = recognizer.recognize_google(audio, language='en-in')
    #             message = message.lower()
    #             print(f"Me: {message}")

    #         assistant.request(message)
    #     except sr.UnknownValueError:
    #         recognizer = sr.Recognizer()


# my_assistant()
