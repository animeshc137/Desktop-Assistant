import requests
import speech_recognition as sr
import pyttsx3
from datetime import *
import time

recognizer = sr.Recognizer()

"""VOICE"""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # object creation
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1


def weather_report():
    global recognizer

    engine.say('Say the city name.')
    engine.runAndWait()

    done = False

    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.pause_threshold = 0.6
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)

                location = recognizer.recognize_google(audio, language='en-in')
                location = location.lower()
                # print(location)
                # location = input('Enter location: ')
                done = True

                api = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=06c921750b9a82d8f5d1294e1586276f"

                json_data = requests.get(api).json()
                condition = json_data['weather'][0]['main']
                temp = int(json_data['main']['temp'] - 273.15)
                min_temp = int(json_data['main']['temp_min'] - 273.15)
                max_temp = int(json_data['main']['temp_max'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']
                sunrise = time.strftime('%I:%M', time.gmtime(
                    json_data['sys']['sunrise'] - 19800))
                sunset = time.strftime('%I:%M', time.gmtime(
                    json_data['sys']['sunset'] - 19800))
                date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
                print("-------------------------------------------------------------")
                print(
                    f"# Weather Stats for - {location.upper()} || {date_time}")
                print("-------------------------------------------------------------")
                print(f"- Condition: {condition}")
                print(f"- Temprature: {temp:.2f} °C")
                print(f"- Minimum Temprature: {min_temp} °C")
                print(f"- Maximum Temprature: {max_temp} °C")
                print(f"- Pressure: {pressure} square inch")
                print(f"- Humidity: {humidity} %")
                print(f"- Wind: {wind} knot")
                print(f"- Sunrise: {sunrise} AM")
                print(f"- Sunset: {sunset} PM\n")

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            engine.say('I did not understand. Please try again!')
            engine.runAndWait()


# weather_report()
