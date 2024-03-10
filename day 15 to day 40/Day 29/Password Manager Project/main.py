from tkinter import *
from tkinter import messagebox
from password_generator import create_password
import pandas as pd
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    _new_password = create_password()
    password.delete(0, END)
    password.insert(0, _new_password)
    pyperclip.copy(_new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    _website_name = website.get()
    _email_user = email.get()
    _password = password.get()

    if _website_name == '' or _email_user == '' or _password == '':
        messagebox.showinfo(title="Error", message="Please, fill all the entries")
    elif any(char in _password for char in [";", " "]):
        messagebox.showinfo(title="Error", message="The password must not have ';' or space")
    elif _website_name.__contains__(";"):
        messagebox.showinfo(title="Error", message="The website must not have ';'")
    elif any(char in _email_user for char in [";", " "]):
        messagebox.showinfo(title="Error", message="The email must not have ';' or space")
    else:
        check_info = messagebox.askokcancel(title=_website_name, message=f"These are the details entered:"
                                                                         f"\nEmail: {_email_user}\nPassword: {_password}"
                                                                         f"\nIs it ok to save?")
        if check_info:
            website.delete(0, END)
            password.delete(0, END)
            with open("passwords_file.csv", "a") as file:
                file.write(f"{_website_name};{_email_user};{_password}\n")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(70, 100, image=img)
# the args are the x and y position of the image
canvas.grid(column=1, row=0)

Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

website = Entry(width=40)
website.grid(column=1, row=1, columnspan=2)
website.focus()

email = Entry(width=40)
email.grid(column=1, row=2, columnspan=2)

column_names = ['website', 'email/user', 'password']
df = pd.read_csv('passwords_file.csv', names=column_names, sep=';')
if not df.empty:
    # Find the most common email/user to insert while opening
    most_common_user = df['email/user'].value_counts().idxmax()
else:
    most_common_user = ""

email.insert(0, most_common_user)

password = Entry(width=21)
password.grid(column=1, row=3, padx=(6, 115))

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=1, row=3, padx=(140, 0))

add_button = Button(text="Add", command=add_password, width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
