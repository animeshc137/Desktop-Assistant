import sqlite3
from tkinter import *
from tkinter import messagebox
import time
import os

# Connect to sqlite database
conn = sqlite3.connect('database/database.db')
c = conn.cursor()

'''Time'''
time = time.strftime("%H:%M %a, %b %d,%Y")


c.execute(
    "CREATE TABLE IF NOT EXISTS users(username NOT NULL PRIMARY KEY, email TEXT, password VARCHAR, timestamp TEXT)")


def check_signup(username, email, password, reg_username_entry):
    try:
        global c
        global time
        c.execute("select * from users where username=?", (username,))

        details = c.fetchone()
        if details != None:
            reg_username_entry.delete(0, END)
            messagebox.showerror(
                "Error !", "Username already exist! Try with another.")
        else:
            c.execute(
                f"INSERT INTO users(username, email, password, timestamp) VALUES('{username}', '{email} ', '{password}', '{time}')")
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

        c.execute("select * from users where username=? and password=?",
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
            "CREATE TABLE IF NOT EXISTS files(username NOT NULL PRIMARY KEY, files TEXT, time TEXT)")
        c.execute(
            f"INSERT INTO files(username, files, time) VALUES('{username}', '{file_name}', '{time}')")
        conn.commit()
        print("successfully inserted!!")
    except sqlite3.Error as error:
        messagebox.showerror(
            "Problem with SQlite table, Contact the developer!!", message=f"{error}")
