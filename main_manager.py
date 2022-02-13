from window_ui import *

# Name: Ruben Sanduleac
# Description:

WINDOW_NAME = "Password Manager"


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
    # objects for the website, username and password that will be used to save the info
    web_entry = Entry()
    username_entry = Entry()
    password_entry = Entry()
    main_window_labels()
    # configure the location of entries in the
    entry_config(web_entry, username_entry, password_entry)
    # function call for the "add" a button
    write_buttton(web_entry, username_entry, password_entry)
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
