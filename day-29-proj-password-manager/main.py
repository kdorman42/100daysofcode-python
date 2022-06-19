from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

BG_COLOR = '#ffffff'
FG_COLOR = '#000000'
FONT_TUPLE = ("Arial", 10, "normal")
EMAIL = 'fake_email_address@gmail.com'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    username_input = username_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "username": username_input,
            "password": password_input
        }
    }

    if website_input == '' or username_input == '' or password_input == '':
        messagebox.showerror(title="Oops", message="Please fill in all fields!")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)  # read old data
                data.update(new_data)  # update with new data
        except FileNotFoundError:
            data = new_data
        except UnboundLocalError:
            data = new_data
        finally:
            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)  # save to file

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- RETRIEVE PASSWORD ------------------------------- #
def find_password():
    website_input = website_entry.get()
    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data file found.")
    else:
        if website_input in data:
            messagebox.showinfo(title="Website credentials found",
                                message=f"Details for {website_input}:\n\n"
                                f"Username: {data[website_input]['username']}\n"
                                f"Password: {data[website_input]['password']}\n")
        else:
            messagebox.showwarning(title="Oops", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=BG_COLOR)

canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=FONT_TUPLE, fg=FG_COLOR, bg=BG_COLOR)
website_label.grid(column=0, row=1)
website_entry = Entry(width=28)
website_entry.grid(column=1, row=1, sticky='w')
website_entry.focus()  # starts with cursor in website field

username_label = Label(text="Username:", font=FONT_TUPLE, fg=FG_COLOR, bg=BG_COLOR)
username_label.grid(column=0, row=2)
username_entry = Entry(width=50)
username_entry.insert(END, EMAIL)  # index=END starts at the end of whatever text is there
username_entry.grid(column=1, row=2, columnspan=2, sticky='w', pady=2)

password_label = Label(text="Password:", font=FONT_TUPLE, fg=FG_COLOR, bg=BG_COLOR)
password_label.grid(column=0, row=3)
password_entry = Entry(width=28)
password_entry.grid(column=1, row=3, sticky='w')

search_button = Button(text="Search", bg=BG_COLOR, width=14, command=find_password)
search_button.grid(column=2, row=1, pady=2)
make_password_button = Button(text="Generate Password", bg=BG_COLOR, command=generate_password)
make_password_button.grid(column=2, row=3, pady=2)
add_button = Button(text="Add", width=42, bg=BG_COLOR, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=2, sticky='w')

window.mainloop()
