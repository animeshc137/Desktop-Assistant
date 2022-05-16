# from tkinter import *
# from PIL import Image, ImageTk

# window = Tk()
# window.title("Desktop Assistant")
# windowWidth = window.winfo_reqwidth()
# windowHeight = window.winfo_reqheight()
# positionRight = int(window.winfo_screenwidth()/2 - 982/2)
# positionDown = int(window.winfo_screenheight()/2 - 710/2)
# window.geometry(f"982x629+{positionRight}+{positionDown}")
# window.iconbitmap('images/favicon.ico')
# # window.wm_attributes('-alpha', 0.7)
# window.configure(bg="#fff")
# canvas = Canvas(window, bg="#fff", height=629, width=982,
#                 bd=0, highlightthickness=0, relief="ridge")
# canvas.place(x=0, y=0)


# '''Final Page'''
# img = ImageTk.PhotoImage(file="images/logo1.png")
# canvas.create_image(50, 40, image=img)

# wizard = ImageTk.PhotoImage(file="images/wizard.png")
# canvas.create_image(500, 220, image=wizard, tag='wizard')

# Rectangle_box = ImageTk.PhotoImage(file="images/Rectangle 9.png")
# canvas.create_image(500, 490, image=Rectangle_box, tag='Rectangle_box')


# ball_1 = ImageTk.PhotoImage(file="images/ball 1.png")
# canvas.create_image(720, 200, image=ball_1, tag='ball_1')

# ball_2 = ImageTk.PhotoImage(file="images/ball 2.png")
# canvas.create_image(60, 350, image=ball_2, tag='ball_2')

# ball_3 = ImageTk.PhotoImage(file="images/ball 3.png")
# canvas.create_image(260, 170, image=ball_3, tag='ball_3')

# ball_4 = ImageTk.PhotoImage(file="images/ball 4.png")
# canvas.create_image(790, 330, image=ball_4, tag='ball_4')

# ball_5 = ImageTk.PhotoImage(file="images/ball 5.png")
# canvas.create_image(950, 150, image=ball_5, tag='ball_5')

# ball_6 = ImageTk.PhotoImage(file="images/ball 6.png")
# canvas.create_image(200, 350, image=ball_6, tag='ball_6')

# window.mainloop()


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


if __name__ == '__main__':

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
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

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
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
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

time.sleep(3)
