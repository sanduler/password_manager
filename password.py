# Name: Ruben Sanduleac
# Description:
import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


def clear_password(web_entry, username_entry, password_entry):
    """[This function clears everything in the gui after password is saved to the json]
    Args:
        web_entry ([object]): [user entry object for the website title.]
        username_entry ([object]): [user entry object for the username.]
        password_entry ([object]): [user entry object for the password.]
    """
    # delete the strings from the objects
    web_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def generate_password(password_entry):
    """[This function uses a preset lists with the whole alphabet, integers 0-9 and most common symbols
        needed for a password. The program, then randomly picks the needed characters and shuffles the list]
        Args:
            password_entry ([object]): [user entry object for the password.]
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    # randomly choose between 8-10 letters, 2-4 symbols and 2-4 numbers
    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    # concatenate password
    password_list = password_letters + password_symbols + password_numbers
    # shuffle the order randomly
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    # place the password in the clipboard
    pyperclip.copy(password)


def find_password(web_entry):
    """[This function is linked and is called to from search_button.
        it is responsible for searching for the username and password
        for the specified web entry. if no web entry is not present the
        function gives out an error. Finally, if there is no file the
        function creates the file. If there is no detail in the database
        then return.
            Args:
                web_entry ([object]): [user entry for the website.]
    """
    # get the data from the web_entry object
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
