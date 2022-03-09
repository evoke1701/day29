from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pw():

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    ent_password.delete(0, END)
    # if len(ent_password) == 0:
    ent_password.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_input():
    website_input = ent_website.get()
    username_input = ent_emailusername.get()
    password = ent_password.get()
    if len(website_input) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Don't leave any entries empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website_input,
            message=f"These are the detials entered: \nEmail: {username_input} "
            f"\nPassword: {password} \nIs it ok to save?",
        )
        if is_ok:
            with open("passwords.txt", "a") as passwords:
                print(
                    f"{website_input} | {username_input} | {password}\n", file=passwords
                )
                clear_input()


def clear_input():
    ent_website.delete(0, END)
    ent_emailusername.delete(0, END)
    ent_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("EVOKES COOL PASSWORD MANAGER")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=180, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=logo)
canvas.grid(column=1, row=0)


# Labels
l_website = Label(text="Website:")
l_website.grid(column=0, row=1, sticky="e")
l_emailusername = Label(text="Email/Username:")
l_emailusername.grid(column=0, row=2, sticky="e")
l_password = Label(text="Password:")
l_password.grid(column=0, row=3, sticky="e")


# Entries

ent_website = Entry(width=52)
ent_website.grid(column=1, row=1, columnspan=2, sticky="ew")
ent_website.focus()
ent_emailusername = Entry(width=52)
ent_emailusername.grid(column=1, row=2, columnspan=2, sticky="ew")
ent_emailusername.insert(0, "evoked@gmail.com")
ent_password = Entry(width=33)
ent_password.grid(column=1, row=3, sticky="w", padx=0, pady=0)

# Buttons

b_generatepw = Button(text="Generate Password", command=generate_pw)
b_generatepw.grid(column=2, row=3, sticky="ew")


b_add = Button(text="Add", width=35, command=save_input)
b_add.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
