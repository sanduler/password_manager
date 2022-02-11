# Name: Ruben Sanduleac
# Description:
from tkinter import *
import tkinter.messagebox
import pyperclip
from random import choice, randint, shuffle

WINDOW_NAME = "Password Manager"


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


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


# ------------------------------------ TODO: UI ---------------------------------------
# TODO: develop a window for the program
window = Tk()
window.title(WINDOW_NAME)
window.config(padx=20, pady=20)
# TODO: implement a canvas for the logo
canvas = Canvas(width=200, height=200)
# TODO: link canvas logo to the window
logo = PhotoImage(file="img/logo.png")
canvas.create_image(75, 100, image=logo)
# canvas.config(bg="blue")
canvas.grid(column=1, row=0, columnspan=2)

# TODO: develop a text input column for typing the website that will be used to save the password
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
web_entry = Entry()
web_entry.config(width=37)
web_entry.grid(column=1, row=1, columnspan=2)

# TODO: implement an input column for the email address/username that
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry()
username_entry.config(width=37)
# at the start the program automatically starts the input at the username
username_entry.focus()
username_entry.grid(column=1, row=2, columnspan=2)

# TODO: implement an input column for password
# TODO: make sure the password field is hidden
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

# TODO: implement a button on the bottom to save the password externally --> if possible to text
add_button = Button(text="Add", command=save)
add_button.config(width=35)
add_button.grid(column=1, row=4, columnspan=2)

# TODO: implement a button next to the password generate a new password
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.config(width=11, pady=0)
generate_button.grid(column=2, row=3)

# ------------------------------------ TODO: SAVE PASSWORD ---------------------------------------
# TODO: implement a function responsible for text input column for typing the website
# TODO: implement a function responsible for input column for the email address/username
# TODO: implement a function responsible for input column for the password field
# TODO: implement a function responsible for "generate new password" button
# TODO: implement a function responsible for "add" button
# ---------------------------- TODO: PASSWORD GENERATOR LOGIC ------------------------------- #
# TODO: implement a function responsible for creating a password with a preset strength
window.eval('tk::PlaceWindow . center')
window.mainloop()
