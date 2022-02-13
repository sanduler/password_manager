from password import *


def main_window_labels():
    web_label = Label(text="Website:")
    web_label.grid(column=0, row=1)
    username_label = Label(text="Email/Username:")
    username_label.grid(column=0, row=2)
    password_label = Label(text="Password: ")
    password_label.grid(column=0, row=3)


def entry_config(web_entry, username_entry, password_entry):
    web_entry.config(width=21)
    web_entry.grid(column=1, row=1)
    password_entry.config(width=21)
    password_entry.grid(column=1, row=3)
    username_entry.config(width=37)
    # at the start the program automatically starts the input at the username
    username_entry.focus()
    username_entry.grid(column=1, row=2, columnspan=2)


def generate_button(password):
    # create the button for generating a password
    create_button = Button(text="Generate Password", command=lambda: generate_password(password))
    create_button.config(width=11, pady=0)
    create_button.grid(column=2, row=3)


def search_button(web_entry):
    """a button on the bottom to search the password externally --> if possible to text"""
    add_button = Button(text="Search", command=lambda: find_password(web_entry))
    add_button.config(width=11, pady=0)
    add_button.grid(column=2, row=1)


def write_buttton(web, username, password):
    """a button on the bottom to save the password externally --> if possible to text"""
    add_button = Button(text="Add", command=lambda: save_password(web, username, password))
    add_button.config(width=35)
    add_button.grid(column=1, row=4, columnspan=2)
