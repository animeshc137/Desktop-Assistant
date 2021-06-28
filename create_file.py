from voice_recognizer import *
from os import path
import db_connect

'''Create file'''


def create_file(username):
    global recognizer

    print("Bot: What do you want to write onto your file?")
    engine.say("What do you want to write onto your file?")
    engine.runAndWait()

    done = False

    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.pause_threshold = 0.6
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio, language='en-in')
                note = note.lower()
                print(f"Me: {note}")

                exist = False
                print("Bot: choose a file name!")
                engine.say("choose a file name!")
                engine.runAndWait()

                while not exist:
                    try:
                        recognizer.pause_threshold = 0.6
                        recognizer.adjust_for_ambient_noise(mic)
                        audio = recognizer.listen(mic)

                        file_name = recognizer.recognize_google(
                            audio, language='en-in')
                        file_name = file_name.lower() + '.txt'
                        print(f"Me: {file_name}")
                        file_present = path.exists(
                            f"files/{username}/{file_name}")

                        if file_present == False:
                            print(username)

                            with open(f"files/{username}/{file_name}", "w") as f:
                                f.write(note)
                                print(
                                    f"Bot: I succesfully created the file {file_name}")
                                engine.say(
                                    f"I succesfully created the file {file_name}")
                                engine.runAndWait()

                                # db_connect.append_filename(username, file_name)
                                done = True
                                exist = True

                        else:
                            print(
                                "Bot: Sorry file already exist!! Choose another file name.")
                            engine.say(
                                "Sorry file already exist!! Choose another file name.")
                            engine.runAndWait()

                    except sr.UnknownValueError:
                        recognizer = sr.Recognizer()
                        print(
                            'Bot: I did not understant you! Please try again!')
                        engine.say(
                            'I did not understant you! Please try again!')
                        engine.runAndWait()
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            print(
                'Bot: I did not understant you! Please try again!')
            engine.say(
                'I did not understant you! Please try again!')
            engine.runAndWait()


# username = "abhinav19"
# create_file(username)
