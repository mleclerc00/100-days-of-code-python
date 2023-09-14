import random
import string
import tkinter as tk
import tkinter.messagebox as messagebox

import pyperclip as pc

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generate a random password"""
    password_entry.delete(0, tk.END)
    source = string.ascii_letters + string.digits + string.punctuation
    random_password = "".join([random.choice(source) for _ in range(0, 20)])
    password_entry.insert(0, random_password)
    pc.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Save the password to a file"""

    # Get the entries
    website_entry_text = website_entry.get()
    email_entry_text = email_entry.get()
    password_entry_text = password_entry.get()

    # Check if any of the entries are empty
    if len(website_entry_text) == 0 or len(email_entry_text) == 0 or len(password_entry_text) == 0:
        messagebox.showwarning(title="Warning", message="Please make sure you haven't left any fields empty!")
        return

    # Confirm that the user wants to save the password
    confirm = messagebox.askokcancel(
        title="Confirm",
        message=f"Are you sure you want to save this password?\n\nWebsite: {website_entry_text}\nEmail: {email_entry_text}\nPassword: {password_entry_text}",
    )

    # Write the entries to a file
    if confirm:
        with open("./passwords.txt", mode="a") as file:
            file.write(f"{website_entry_text} | {email_entry_text} | {password_entry_text}\n")

            # Clear the entries
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            popup()


# ---------------------------- User Feedback ------------------------------- #


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
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
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

window.mainloop()
