import sqlite3
from tkinter import *
from tkinter import messagebox
import time
import os

# Connect to sqlite database
conn = sqlite3.connect('./database1.db')
c = conn.cursor()

'''Time'''
time = time.strftime("%H:%M %a, %b %d,%Y")

# c.execute("DROP TABLE filo_users;")
# c.execute("DROP TABLE user_files;")

c.execute(
    "CREATE TABLE IF NOT EXISTS filo_users(username NOT NULL PRIMARY KEY, email TEXT, password VARCHAR, timestamp TEXT)")


def check_signup(username, email, password, reg_username_entry):
    try:
        global c
        global time
        c.execute("select * from filo_users where username=?", (username,))

        details = c.fetchone()
        if details != None:
            reg_username_entry.delete(0, END)
            messagebox.showerror(
                "Error !", "Username already exist! Try with another.")
        else:
            c.execute(
                f"INSERT INTO filo_users(username, email, password, timestamp) VALUES('{username}', '{email} ', '{password}', '{time}')")
            conn.commit()
            messagebox.showinfo(message="Signup Successfully!")
            os.mkdir(f"files/{username}")

            return True

    except sqlite3.Error as error:
        messagebox.showerror(
            "Problem with SQlite table, Contact the developer!!", message=f"{error}")


def check_login(username, password):
    try:
        global c

        c.execute("select * from filo_users where username=? and password=?",
                  (username, password))

        details = c.fetchone()
        if details != None:
            messagebox.showinfo(message="Login Successfully!")

            return True

        else:
            messagebox.showerror("Error !", "Invalid Username or Password !")

    except sqlite3.Error as error:
        messagebox.showerror(
            "Problem with SQlite table, Contact the developer!!", message=f"{error}")


def append_filename(username, file_name):
    try:
        c.execute(
            f"""CREATE TABLE IF NOT EXISTS user_files(
            file_id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_user VARCHAR(30) NULL, 
            file_name VARCHAR(30) NOT NULL ,
            time TEXT, 
            FOREIGN KEY (file_user) REFERENCES filo_users (username))""")
        c.execute(
            f"INSERT INTO user_files(file_user, file_name, time) VALUES('{username}', '{file_name}', '{time}')")
        conn.commit()
        # conn.close()
        print("successfully inserted!!")
    except sqlite3.Error as error:
        messagebox.showerror(
            "Problem with SQlite table, Contact the developer!!", message=f"{error}")


# username = 'patel'
# email = 'patel@gmail.com'
# password = '1'
# reg_username_entry = 'patel'
# file_name = 'mongo'

# append_filename(username, file_name)
# c.execute("select file_name from user_files where file_user=?", (username,))
# # check_signup(username, email, password, reg_username_entry)
# details = c.fetchall()
# print(details)
