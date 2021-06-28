from voice_recognizer import *
from os import listdir
# import db_connect

'''show file'''


def show_files(username):
    engine.say('The files on your directory are the following: ')
    files_list = listdir(f"files/{username}/")
    print(files_list)
    engine.runAndWait()
