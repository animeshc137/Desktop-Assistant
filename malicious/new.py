# from neuralintents import GenericAssistant
# import speech_recognition as sr
# import pyttsx3
# from os import path
# import sys
# import glob

# """VOICE"""
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')  # object creation
# engine.setProperty('voice', voices[1].id)  # female voice
# engine.setProperty('rate', 180)
# engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

# recognizer = sr.Recognizer()

# # todo_list = ['go shopping', 'clean room', 'record video']

# # for file_name in glob.iglob('files/*.txt', recursive=True):
# #     # engine.say(file_name)
# #     # engine.runAndWait()
# #     print(file_name)

# txt_files = []


# def create_file():
#     global recognizer

#     engine.say("What do you want to write onto your file?")
#     engine.runAndWait()

#     done = False

#     while not done:
#         try:
#             with sr.Microphone() as mic:
#                 recognizer.adjust_for_ambient_noise(mic)
#                 audio = recognizer.listen(mic)

#                 note = recognizer.recognize_google(audio, language='en-in')
#                 note = note.lower()

#                 exist = False

#                 engine.say("choose a file name!")
#                 engine.runAndWait()

#                 while not exist:
#                     try:

#                         recognizer.adjust_for_ambient_noise(mic)
#                         audio = recognizer.listen(mic)

#                         file_name = recognizer.recognize_google(
#                             audio, language='en-in')
#                         file_name = file_name.lower() + '.txt'
#                         file_present = path.exists(f"files/{file_name}")

#                         if file_present == False:

#                             with open(f"files/{file_name}", "w") as f:
#                                 f.write(note)
#                                 done = True
#                                 exist = True
#                                 engine.say(
#                                     f"I succesfully created the file {file_name}")
#                                 engine.runAndWait()
#                                 for file_name in glob.glob("*.txt"):
#                                     txt_files.append(file_name)

#                         else:
#                             engine.say(
#                                 "Sorry file already exist!! Choose another file name.")
#                             engine.runAndWait()

#                     except sr.UnknownValueError:
#                         recognizer = sr.Recognizer()
#                         engine.say(
#                             'I did not understant you! Please try again!')
#                         engine.runAndWait()
#         except sr.UnknownValueError:
#             recognizer = sr.Recognizer()
#             engine.say(
#                 'I did not understant you! Please try again!')
#             engine.runAndWait()


# def update_file():
#     global recognizer

#     engine.say('What do you want to add in your file.')
#     engine.runAndWait()
#     done = False

#     while not done:
#         try:
#             with sr.Microphone() as mic:
#                 recognizer.adjust_for_ambient_noise(mic)
#                 audio = recognizer.listen(mic)

#                 item = recognizer.recognize_google(audio, language='en-in')
#                 item = item.lower()

#                 txt_files.append(item)
#                 done = True

#                 engine.say(f'I add {item} to the to do list!')
#                 engine.runAndWait()
#         except sr.UnknownValueError:
#             recognizer = sr.Recognizer()
#             engine.say('I did not understand. Please try again!')
#             engine.runAndWait()


# def show_files():
#     engine.say('The files on your directory are the following')
#     for item in txt_files:
#         engine.say(item)
#     engine.runAndWait()


# def greetings():
#     engine.say('Hello sir, what i can do for you?')
#     engine.runAndWait()


# def quit():
#     engine.say('See you soon, have a nice day!!')
#     engine.runAndWait()
#     sys.exit(0)


# mappings = {
#     'greeting': greetings,
#     'create_file': create_file,
#     'update_file': update_file,
#     'show_files': show_files,
#     'exit': quit
# }


# assistant = GenericAssistant(
#     'data/intents.json', intent_methods=mappings)
# # assistant.train_model()
# # assistant.save_model(model_name="data/test_model")
# assistant.load_model(model_name="data/test_model")

# while True:
#     try:
#         with sr.Microphone() as mic:
#             recognizer.adjust_for_ambient_noise(mic)
#             print("Speak: ", end=" ")
#             audio = recognizer.listen(mic)

#             message = recognizer.recognize_google(audio, language='en-in')
#             message = message.lower()

#         assistant.request(message)
#     except sr.UnknownValueError:
#         recognizer = sr.Recognizer()

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
# from ecapture import ecapture as ec
import wolframalpha
import json
import requests


print('Loading your AI personal assistant - G One')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your AI personal assistant G-One")
wishMe()


# if __name__ == '__main__':
while True:
    speak("Tell me how can I help you now?")
    statement = takeCommand().lower()
    if statement == 0:
        continue
    if "good bye" in statement or "ok bye" in statement or "stop" in statement:
        speak('your personal assistant G-one is shutting down,Good bye')
        print('your personal assistant G-one is shutting down,Good bye')
        break
    if 'wikipedia' in statement:
        speak('Searching Wikipedia...')
        statement = statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        time.sleep(5)
    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        time.sleep(5)
    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now")
        time.sleep(5)
    elif "weather" in statement:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("whats the city name")
        city_name = takeCommand()
        complete_url = base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
                  str(current_temperature) +
                  "\n humidity in percentage is " +
                  str(current_humidiy) +
                  "\n description  " +
                  str(weather_description))
            print(" Temperature in kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
        else:
            speak(" City Not Found ")
    elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
    elif 'who are you' in statement or 'what can you do' in statement:
        speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
              'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipediapredict weather'
              'in different cities , get top headline news from times of india and you can ask me computationalor geographical questions too!')
    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("I was built by Mirthula")
        print("I was built by Mirthula")
    elif "open stackoverflow" in statement:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        speak("Here is stackoverflow")
    elif 'news' in statement:
        news = webbrowser.open_new_tab(
            "https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)
    # elif "camera" in statement or "take a photo" in statement:
    #     ec.capture(0, "robo camera", "img.jpg")
    elif 'search' in statement:
        statement = statement.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(5)
    elif 'ask' in statement:
        speak('I can answer to computational and geographical questions and what question do you want to asknow')
        question = takeCommand()
        app_id = "R2K75H-7ELALHR35X"
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
        print(answer)
    elif "log off" in statement or "sign out" in statement:
        speak(
            "Ok , your pc will log off in 10 sec make sure you exit from all applications")
        subprocess.call(["shutdown", "/l"])
tim.sleep(3)
