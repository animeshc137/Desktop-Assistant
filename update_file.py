from voice_recognizer import *
from os import path, remove, rename
import db_connect

'''update file (Animesh)'''


def update_file(username):

    global recognizer

    engine.say("Choose a file to update.")
    engine.runAndWait()

    choose_file = False
    while not choose_file:
        try:
            with sr.Microphone() as mic:
                recognizer.pause_threshold = 0.6
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)
                file_name = recognizer.recognize_google(
                    audio, language='en-in')
                file_name = file_name.lower() + '.txt'
                print(file_name)

                file_present = path.exists(
                    f"files/{username}/{file_name}")

                if file_present == True:

                    choose_file = True
                    engine.say("""Which action do you want to performed in the file.
                                You can clear everything and start fresh
                                Append to the file.
                                Replace a certain word with a new word
                                Or You can delete the file entirely""")

                    engine.runAndWait()

                    operation_performed = False
                    while not operation_performed:
                        try:
                            with sr.Microphone() as mic:
                                recognizer.pause_threshold = 0.6
                                recognizer.adjust_for_ambient_noise(mic)
                                audio = recognizer.listen(mic)
                                operation = recognizer.recognize_google(
                                    audio, language='en-in')
                                operation = operation.lower()
                                print(operation)

                                if 'clear' in operation:
                                    try:
                                        file = open(
                                            f"files/{username}/{file_name}", 'r+')
                                        file.truncate(0)
                                        file.close()
                                        engine.say(
                                            "I have cleared the entire file")
                                        engine.runAndWait()
                                        print("I have cleared the entire file")
                                        operation_performed = True
                                    except:
                                        engine.say(
                                            'Exception occured, cant clear the file. Choose another operation!')
                                        engine.runAndWait()

                                elif 'append' in operation:
                                    try:
                                        file = open(
                                            f"files/{username}/{file_name}", "a+")
                                        while True:
                                            file.write('\n')
                                            engine.say(
                                                f"What do you want to append to the file ?{file_name}")
                                            engine.runAndWait()
                                            recognizer.adjust_for_ambient_noise(
                                                mic)
                                            audio = recognizer.listen(mic)
                                            append_line = recognizer.recognize_google(
                                                audio, language='en-in')
                                            file.write(append_line)
                                            engine.say(
                                                "Do you want to append more lines to the file?")
                                            engine.runAndWait()
                                            recognizer.adjust_for_ambient_noise(
                                                mic)
                                            audio = recognizer.listen(mic)
                                            choice = recognizer.recognize_google(
                                                audio, language='en-in')
                                            print(choice)
                                            if 'no' in choice:
                                                engine.say(
                                                    "Got it, closing the file")
                                                engine.runAndWait()
                                                print(
                                                    "Got it, closing the file")
                                                file.close()
                                                operation_performed = True
                                                break
                                            elif len(choice) == 0:
                                                continue
                                    except:
                                        engine.say(
                                            'Exception occured, cant append to the file. Please try again!')
                                        engine.runAndWait()

                                elif 'replace' in operation:
                                    try:
                                        file_read = open(
                                            f"files/{username}/{file_name}", "rt")
                                        file_write = open(
                                            f"files/{username}/temp.txt", "wt")
                                        engine.say("File Successfully opened")
                                        engine.say(
                                            f"what word/phrase do you want to replace in the file {file_name}?")
                                        engine.runAndWait()
                                        recognizer.adjust_for_ambient_noise(
                                            mic)
                                        audio = recognizer.listen(mic)
                                        replace_phrase = recognizer.recognize_google(
                                            audio, language='en-in')
                                        replace_phrase = replace_phrase.lower()
                                        print(replace_phrase)
                                        engine.say(
                                            "what word/phrase do you want to replace in with?")
                                        engine.runAndWait()
                                        recognizer.adjust_for_ambient_noise(
                                            mic)
                                        audio = recognizer.listen(mic)
                                        phrase = recognizer.recognize_google(
                                            audio, language='en-in')
                                        phrase = phrase.lower()
                                        print(phrase)
                                        for line in file_read:
                                            file_write.write(line.replace(
                                                replace_phrase, phrase))
                                        file_read.close()
                                        file_write.close()
                                        remove(f'files/{username}/{file_name}')
                                        rename(
                                            f'files/{username}/temp.txt', f"files/{username}/{file_name}")
                                        engine.say(
                                            "The changes were made Succesfully!")
                                        operation_performed = True
                                    except:
                                        engine.say(
                                            'Exception occured, cant perform replace operation. Choose another operation!')
                                        engine.runAndWait()
                                elif 'delete' in operation:
                                    try:
                                        file_present = path.exists(
                                            f"files/{username}/{file_name}.txt")

                                        if file_present == True:

                                            remove(
                                                f"files/{username}/{file_name}.txt")

                                            engine.say(
                                                f'I successfully deleted {file_name}.txt to from the directory!')
                                            engine.runAndWait()

                                            operation_performed = True

                                        else:
                                            engine.say(
                                                "Sorry file not found!! Choose another file name.")
                                            engine.runAndWait()
                                    except:
                                        engine.say(
                                            'Exception occured, cant delete the file. Choose another operation!')
                                        engine.runAndWait()
                                else:
                                    engine.say(
                                        "Invalid operation, please try again!")
                                    engine.runAndWait()

                        except sr.UnknownValueError:
                            # recognizer = sr.Recognizer()
                            engine.say(
                                'I did not understant you! Please try again!')
                            engine.runAndWait()
                else:
                    engine.say(
                        "Sorry file doesn't exist!! Choose another file name.")
                    engine.runAndWait()
        except sr.UnknownValueError:
            engine.say(
                'I did not understant you! Please try gain!')
            engine.runAndWait()


# username = "abhinav19"
# update_file(username)
