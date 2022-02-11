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
canvas = Canvas(width=400, height=400)
# TODO: link canvas logo to the window
logo = PhotoImage(file="img/logo.png")
canvas.create_image(200, 200, image=logo)
canvas.pack()
# TODO: develop a text input column for typing the website that will be used to save the password
# TODO: implement an input column for the email address/username that
# TODO: implement an input column for password
# TODO: make sure the password field is hidden
# TODO: implement a button next to the password generate a new password
# TODO: implement a button on the bottom to save the password externally --> if possible to text

# ------------------------------------ TODO: SAVE PASSWORD ---------------------------------------
# TODO: implement a function responsible for text input column for typing the website
# TODO: implement a function responsible for input column for the email address/username
# TODO: implement a function responsible for input column for the password field
# TODO: implement a function responsible for "generate new password" button
# TODO: implement a function responsible for "add" button

# ---------------------------- TODO: PASSWORD GENERATOR LOGIC ------------------------------- #
# TODO: implement a function responsible for creating a password with a preset strength

window.mainloop()