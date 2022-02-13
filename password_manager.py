# Name: Ruben Sanduleac
# Description: The main manager is the entry point for the password manager.
#              the main functions initializes all the labels, buttons and the canvas.
#              The main window passes the web_entry, username and password.

from window_ui import *

WINDOW_NAME = "Password Manager"


def main():
    # generate a window using the tkinter class
    window = Tk()
    # change the name of the window
    window.title(WINDOW_NAME)
    # set the size pf tje padding between canvas and the windows
    window.config(padx=20, pady=20)
    # canvas for the logo
    canvas = Canvas(width=200, height=200)
    # logo to the window
    logo = PhotoImage(file="img/logo.png")
    # add the image to the window
    canvas.create_image(75, 100, image=logo)
    # canvas.config(bg="blue")
    canvas.grid(column=1, row=0, columnspan=2)
    # objects for the website, username and password that will be used to save the info
    web_entry = Entry()
    username_entry = Entry()
    password_entry = Entry()
    # add the labels to the window
    main_window_labels()
    # configure the location of entries in the
    entry_config(web_entry, username_entry, password_entry)
    # function call for the "add" a button
    write_button(web_entry, username_entry, password_entry)
    # function call for generate__button
    generate_button(password_entry)
    # function call for generate__button
    search_button(web_entry)
    # center the window upon opening
    window.eval('tk::PlaceWindow . center')
    # loop the main window to stay open
    window.mainloop()


if __name__ == "__main__":
    main()
