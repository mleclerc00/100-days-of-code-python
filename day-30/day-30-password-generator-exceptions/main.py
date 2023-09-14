import json
import random
import string
import tkinter as tk
import tkinter.messagebox as messagebox

import pyperclip as pc

# ---------------------------- GENERATE PASSWORD ------------------------------- #


def generate_password():
    """Generate a random password"""
    password_entry.delete(0, tk.END)
    source = string.ascii_letters + string.digits + string.punctuation
    random_password = "".join([random.choice(source) for _ in range(0, 20)])
    password_entry.insert(0, random_password)
    pc.copy(random_password)


# ---------------------------- READ PASSWORD FILE ------------------------------- #


def read_password_file():
    """Read the password file"""
    try:
        with open("./passwords.json", mode="r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        write_password_file({})
        return {}


# ---------------------------- WRITE PASSWORD FILE ------------------------------- #


def write_password_file(data):
    """Write the password file"""
    with open("./passwords.json", mode="w") as file:
        json.dump(data, file, indent=4)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    """Find the password for a given website"""
    website = website_entry.get().upper()
    data = read_password_file()
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(
            title=website, message=f"Email: {email}\nPassword: {password} \n\nPassword copied to clipboard."
        )
        pc.copy(password)
    else:
        messagebox.showwarning(title="Warning", message=f"No details for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Save the password to a file"""

    # Get the entries
    website_entry_text = website_entry.get().upper()
    email_entry_text = email_entry.get()
    password_entry_text = password_entry.get()

    entry = {website_entry_text: {"email": email_entry_text, "password": password_entry_text}}

    # Check if any of the entries are empty
    if len(website_entry_text) == 0 or len(email_entry_text) == 0 or len(password_entry_text) == 0:
        messagebox.showwarning(title="Warning", message="Please make sure you haven't left any fields empty!")
        return
    else:
        # read data
        data = read_password_file()
        # update old data with new data
        data.update(entry)
        # save updated data
        write_password_file(data)

        # Clear the entries
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        popup()


# ---------------------------- PASSWORD SAVED FEEDBACK ------------------------------- #


def popup():
    """Create a popup window to notify the user that the password has been saved"""

    # Create a popup window
    messagebox.showinfo(title="Success", message="Your password has been saved!")


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
logo_img = tk.PhotoImage(file="logo.png")

# Canvas
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = tk.Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@gmail.com")

password_entry = tk.Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = tk.Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tk.Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
