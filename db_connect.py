import sqlite3
from tkinter import *
from tkinter import messagebox


# Connect to sqlite database
conn = sqlite3.connect('database/database.db')
c = conn.cursor()

c.execute(
    "CREATE TABLE IF NOT EXISTS users(user_id INTEGER, username NOT NULL PRIMARY KEY, email TEXT, password VARCHAR)")


def check_signup(username, email, password, reg_username_entry):
    try:
        global c

        c.execute("select * from users where username=?", (username,))

        details = c.fetchone()
        if details != None:
            reg_username_entry.delete(0, END)
            messagebox.showerror(
                "Error !", "Username already exist! Try with another.")
        else:
            c.execute(
                f"INSERT INTO users(username, email, password) VALUES('{username}', '{email} ', '{password}')")
            conn.commit()
            messagebox.showinfo(message="Signup Successfully!")

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

        else:
            messagebox.showerror("Error !", "Invalid Username or Password !")

    except sqlite3.Error as error:
        messagebox.showerror(
            "Problem with SQlite table, Contact the developer!!", message=f"{error}")
