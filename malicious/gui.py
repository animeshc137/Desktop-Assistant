# from tkinter import *
# import pyttsx3
# import datetime
# import speech_recognition as sr
# from PIL import Image, ImageTk

# root = Tk()  # using tk() to create a window
# root.title("Desktop Assistant")  # giving title to the window
# root.iconphoto(True, PhotoImage(file='images/logo192.png'))
# # root.geometry("800x600")
# canvas = Canvas(root, width=800, height=600)  # window's dimensions
# canvas.grid(columnspan=3, rowspan=3)

# banner = Image.open('images/space.png')
# banner = ImageTk.PhotoImage(banner)
# banner_label = Label(image=banner)
# banner_label.image = banner
# banner_label.grid(column=0, row=0)


# logo = Image.open('images/logo.png')
# logo = ImageTk.PhotoImage(logo)
# logo_label = Label(image=logo)
# logo_label.image = logo
# logo_label.grid(column=1, row=0)


# login = Label(root, text="Login", font=(
#     'calibre', 10, 'bold'), foreground='black').grid(column=1, row=1)
# name_label = Label(root, text='Enter the temprature: ',
#                    font=('calibre', 10, 'bold'), foreground='black')
# name_entry = Entry(root, font=('calibre', 10, 'normal'))
# name_label.grid(column=0, row=2)
# name_entry.grid(column=1, row=2)


# my_name = 'Abhinav'


# def Greet(audio):
#     engine.say(audio)
#     engine.runAndWait()


# Greet(f"hello {my_name}!")


# # r = sr.Recognizer()
# # keyword = "hello"
# # with sr.Microphone() as source:
# #     print("Speak:", end=" ")
# #     r.pause_threshold = 1
# #     audio = r.listen(source)

# # try:
# #     if r.recognize_google(audio) == keyword:
# #         Greet(f"hello {my_name}!")
# # except sr.UnknownValueError:
# #     print("Could not understand audio")
# root.mainloop()

# # Import the required library
# from tkinter import *

# # Create an instance of tkinter frame
# win = Tk()

# # Define the geometry of the window
# win.geometry("650x450")

# # Define function to hide the widget


# def hide_widget(widget):
#     widget.pack_forget()

# # Define a function to show the widget


# def show_widget(widget):
#     widget.pack()


# # Create an Label Widget
# label = Label(win, text="Showing the Message", font=('Helvetica bold', 14))
# label.pack(pady=20)

# # Create a button Widget
# button_hide = Button(win, text="Hide", command=lambda: hide_widget(label))
# button_hide.pack(pady=20)

# button_show = Button(win, text="Show", command=lambda: show_widget(label))
# button_show.pack()

# win.mainloop()

# from tkinter import Tk, Frame, Canvas, Label
# from PIL import ImageTk

# t = Tk()
# t.title("Transparency")

# frame = Frame(t)
# frame.pack()

# canvas = Canvas(frame, bg="blue", width=500, height=500)
# canvas.pack()

# photoimage = ImageTk.PhotoImage(file="images/logo1.png")
# # photo = Label(t, image=photoimage)
# canvas.create_image(40, 20, image=photoimage)
# # photo.place(x=0, y=0)

# t.mainloop()
