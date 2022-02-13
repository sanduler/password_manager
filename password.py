# Name: Ruben Sanduleac
# Description:
from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle
import json


def clear_password(web_entry, username_entry, password_entry):
    web_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def generate_password(password_entry):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def find_password(web_entry):
    website = web_entry.get()
    try:
        opened_file = open("data/password_data.json", "r")
        data = json.load(opened_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data in file found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {website} exists.")


def save_password(web_entry, username_entry, password_entry):
    password_string = password_entry.get()
    username_string = username_entry.get()
    website_string = web_entry.get()
    new_data = {
        website_string: {
            "email": username_string,
            "password": password_string
        }}
    if len(website_string) != 0 and len(username_string) != 0 and len(password_string) != 0:
        messagebox.askokcancel(message=f"These are the details entered: "
                                       f"\nUsername: {username_string}\nPassword: {password_string}")
        try:
            opened_file = open("data/password_data.json", "r")
            data = json.load(opened_file)
            # updating old data with new data
        except FileNotFoundError:
            opened_file = open("data/password_data.json", "w")
            json.dump(new_data, opened_file, indent=4)
        else:
            data.update(new_data)
            # we close the file
            opened_file.close()
            opened_file = open("data/password_data.json", "w")
            # we dump/save the new data
            json.dump(data, opened_file, indent=4)
            # we close the file
            opened_file.close()
            messagebox.showinfo(message=f"Password for {website_string} was saved.")
    else:
        messagebox.showwarning(message="Please enter all the required information.")

    clear_password(web_entry, username_entry, password_entry)
