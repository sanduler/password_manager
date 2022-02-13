from tkinter import *
import tkinter.messagebox
from generate_password import generate_password
import json

# Name: Ruben Sanduleac
# Description:

WINDOW_NAME = "Password Manager"
WEB_ENTRY = None
USERNAME_ENTRY = None
PASSWORD_ENTRY = None


def clear_entry():
    WEB_ENTRY.delete(0, END)
    USERNAME_ENTRY.delete(0, END)
    PASSWORD_ENTRY.delete(0, END)


def save():
    password_string = PASSWORD_ENTRY.get()
    username_string = USERNAME_ENTRY.get()
    website_string = WEB_ENTRY.get()
    new_data = {
        website_string: {
            "email": username_string,
            "password": password_string
    }}
    if len(website_string) != 0 and len(username_string) != 0 and len(password_string) != 0:
        tkinter.messagebox.askokcancel(message=f"These are the details entered: "
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

        tkinter.messagebox.showinfo(message=f"Password for {website_string} was saved.")
    else:
        tkinter.messagebox.showwarning(message="Please enter all the required information.")

    clear_entry()


def generate__button():
    # create the button for generating a password
    generate_button = Button(text="Generate Password", command=lambda: generate_password(PASSWORD_ENTRY))
    generate_button.config(width=11, pady=0)
    generate_button.grid(column=2, row=3)


def write_buttton():
    """a button on the bottom to save the password externally --> if possible to text"""
    add_button = Button(text="Add", command=save)
    add_button.config(width=35)
    add_button.grid(column=1, row=4, columnspan=2)


def main_window_labels():
    web_label = Label(text="Website:")
    web_label.grid(column=0, row=1)
    username_label = Label(text="Email/Username:")
    username_label.grid(column=0, row=2)
    password_label = Label(text="Password: ")
    password_label.grid(column=0, row=3)


def entry_config():
    WEB_ENTRY.config(width=37)
    WEB_ENTRY.grid(column=1, row=1, columnspan=2)
    PASSWORD_ENTRY.config(width=21)
    PASSWORD_ENTRY.grid(column=1, row=3)
    USERNAME_ENTRY.config(width=37)
    # at the start the program automatically starts the input at the username
    USERNAME_ENTRY.focus()
    USERNAME_ENTRY.grid(column=1, row=2, columnspan=2)


def main():
    window = Tk()
    window.title(WINDOW_NAME)
    window.config(padx=20, pady=20)
    # canvas for the logo
    canvas = Canvas(width=200, height=200)
    # logo to the window
    logo = PhotoImage(file="img/logo.png")
    canvas.create_image(75, 100, image=logo)
    # canvas.config(bg="blue")
    canvas.grid(column=1, row=0, columnspan=2)
    # labels found on the main window
    main_window_labels()
    # objects for the website, username and password that will be used to save the info
    global WEB_ENTRY, USERNAME_ENTRY, PASSWORD_ENTRY
    WEB_ENTRY = Entry()
    USERNAME_ENTRY = Entry()
    PASSWORD_ENTRY = Entry()
    # configure the location of entries in the
    entry_config()
    # function call for the "add" a button
    write_buttton()
    # function call for generate__button
    generate__button()
    # center the window upon opening
    window.eval('tk::PlaceWindow . center')
    # loop the main window to stay open
    window.mainloop()


if __name__ == "__main__":
    main()
