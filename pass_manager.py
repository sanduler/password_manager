# Name: Ruben Sanduleac
# Description:
from tkinter import *
from tkinter.tix import WINDOW

WINDOW_NAME = "Password Manager"
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
username_entry.grid(column=1, row=2, columnspan=2)

# TODO: implement an input column for password
# TODO: make sure the password field is hidden
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.config(width=21, show="*")
password_entry.grid(column=1, row=3)

# TODO: implement a button on the bottom to save the password externally --> if possible to text
add_button = Button(text="Add")
add_button.config(width=35)
add_button.grid(column=1, row=4, columnspan=2)

# TODO: implement a button next to the password generate a new password
generate_button = Button(text="Generate Password",)
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