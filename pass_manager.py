# Name: Ruben Sanduleac
# Description:
from tkinter import *
import tkinter.messagebox
from generate_password import generate_password

WINDOW_NAME = "Password Manager"
web_entry = None
username_entry = None
password_entry = None


def clear_entry():
    web_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def save():
    password_string = password_entry.get()
    username_string = username_entry.get()
    website_string = web_entry.get()
    if len(website_string) != 0 and len(username_string) != 0 and len(password_string) != 0:
        tkinter.messagebox.askokcancel(message=f"These are the details entered: "
                                               f"\nUsername: {username_string}\nPassword: {password_string}")
        file = open("data/passwords.txt", "a")
        file.write(f" {website_string} | {username_string} | {password_string}\n")
        file.close()
        tkinter.messagebox.showinfo(message=f"Password for {website_string} was saved.")
    else:
        tkinter.messagebox.showwarning(message="Please enter all the required information.")

    clear_entry()


def generate__button():
    # create the button for generating a password
    generate_button = Button(text="Generate Password", command=lambda: generate_password(password_entry))
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
    web_entry.config(width=37)
    web_entry.grid(column=1, row=1, columnspan=2)
    password_entry.config(width=21)
    password_entry.grid(column=1, row=3)
    username_entry.config(width=37)
    # at the start the program automatically starts the input at the username
    username_entry.focus()
    username_entry.grid(column=1, row=2, columnspan=2)


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
    # labels found on the mainwindow
    main_window_labels()
    # objects for the website, username and password that will be used to save the info
    global web_entry, username_entry, password_entry
    web_entry = Entry()
    username_entry = Entry()
    password_entry = Entry()
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
