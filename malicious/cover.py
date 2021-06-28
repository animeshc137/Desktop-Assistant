# from tkinter import *
# import webbrowser

# window = Tk()
# window.title("Desktop Assistant")
# windowWidth = window.winfo_reqwidth()
# windowHeight = window.winfo_reqheight()
# positionRight = int(window.winfo_screenwidth()/2 - 862/2)
# positionDown = int(window.winfo_screenheight()/2 - 570/2)
# window.geometry(f"862x519+{positionRight}+{positionDown}")
# window.iconbitmap('images/favicon.ico')
# window.configure(bg="#fff")
# canvas = Canvas(window, bg="#fff", height=519, width=862,
#                 bd=0, highlightthickness=0, relief="ridge")
# canvas.place(x=0, y=0)

# '''cover page'''
# img = PhotoImage(file=f"images/logo1.png")
# logo = Label(window, image=img, background='#fff')
# logo.place(x=15, y=15)

# hero_title = PhotoImage(file=f"images/heroTitle.png")
# title = Label(window, image=hero_title, background='#fff')
# title.place(x=220, y=70)

# bot = PhotoImage(file=f"images/chatbot.png")
# chatbot = Label(window, image=bot, background='#fff')
# chatbot.place(x=300, y=315)

# create_img = PhotoImage(file=f"images/create.png")
# create = Label(window, image=create_img, background='#fff')
# create.place(x=180, y=315)

# read_img = PhotoImage(file=f"images/read.png")
# read = Label(window, image=read_img, background='#fff')
# read.place(x=540, y=340)

# delete_img = PhotoImage(file=f"images/delete.png")
# delete = Label(window, image=delete_img, background='#fff')
# delete.place(x=85, y=420)

# update_img = PhotoImage(file=f"images/update.png")
# update = Label(window, image=update_img, background='#fff')
# update.place(x=555, y=420)

# link_image = PhotoImage(file=f"images/linkTitle.png")
# link_img = Label(window, image=link_image, background='#fff')
# link_img.place(x=750, y=20)


# def contribute_github(event):
#     url = "https://github.com/Abhinav1923/Desktop-Assistant"
#     webbrowser.open_new(url)


# github = Label(text="Contribute on GitHub", bg="#fff",
#                fg="#2B98E7", cursor="hand2")
# github.place(x=715, y=34)
# github.bind('<Button-1>', contribute_github)


# start = PhotoImage(file=f"images/start_button.png")
# start_btn = Button(image=start, borderwidth=0,
#                    highlightthickness=0, relief="flat", background='#fff', cursor="hand2")
# start_btn.place(x=370, y=250)

# window.resizable(False, False)
# window.mainloop()

########################################################################

# import requests
# #import os
# from datetime import datetime

# api_key = 'ce53e6eaa560a79c6fc05fdaae23eff6'
# location = input("Enter the city name: ")

# complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
#     location+"&appid="+api_key
# api_link = requests.get(complete_api_link)
# api_data = api_link.json()

# # create variables to store and display data
# temp_city = ((api_data['main']['temp']) - 273.15)
# weather_desc = api_data['weather'][0]['description']
# hmdt = api_data['main']['humidity']
# wind_spd = api_data['wind']['speed']
# date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# print("-------------------------------------------------------------")
# print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
# print("-------------------------------------------------------------")

# print("Current temperature is: {:.2f} deg C".format(temp_city))
# print("Current weather desc  :", weather_desc)
# print("Current Humidity      :", hmdt, '%')
# print("Current wind speed    :", wind_spd, 'kmph')

# with open("riya_ka_wheater.txt", "a") as f:
#     f.write(f"""
#     -------------------------------------------------------------
#     # Weather Stats for - {location.upper()}  || {date_time}"
#     -------------------------------------------------------------
#     Current temperature is: {temp_city:.2f} deg C"
#     Current weather desc  :", {weather_desc}
#     Current Humidity      :", {hmdt}, '%'
#     Current wind speed    :", {wind_spd}, 'kmph'
#     """)

# import datetime
# import time

# e = datetime.datetime.now()
# time = time.strftime("%a-%b-%d-%Y %I:%M:%S %p")

# print(f"Current date and time = {e}")

# print(f"Today's date:  = {e.day}-{e.month}-{e.year}")

# print(f"The time is now: = {time}")

import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(
        pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()
