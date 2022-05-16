from voice_recognizer import *
from os import listdir
# import db_connect

'''show file'''


def show_files(username):
    engine.say('The files on your directory are the following: ')
    files_list = listdir(f"files/{username}/")
    print(files_list)
    engine.runAndWait()


# # show_files('abhinav19')

# import tkinter as tk
# from tkinter import ttk
# from tkinter import scrolledtext

# # Creating tkinter main window
# win = tk.Tk()
# win.title("ScrolledText Widget")
# win.geometry('600x400')

# # Title Label
# ttk.Label(win,
#           text="ScrolledText Widget Example",
#           font=("Times New Roman", 15),
#           background='green',
#           foreground="white").place(x=0, y=0)

# tri = 'Creating scrolled text'


# def practice():
#     hello = 'hello abhinav'
#     text_area.insert(1.0, hello + '\n')


# # area widget
# text_area = scrolledtext.ScrolledText(win,
#                                       wrap=tk.WORD,
#                                       width=40,
#                                       height=10,
#                                       font=("Times New Roman",
#                                             15))

# # text_area.insert(1.0, tri + '\n')

# text_area.place(x=10, y=30)

# btn = tk.Button(win, text='Click me !', bd='5',
#                 command=practice)
# btn.place(x=300, y=50)


# # Placing cursor in the text area
# text_area.focus()
# win.mainloop()
