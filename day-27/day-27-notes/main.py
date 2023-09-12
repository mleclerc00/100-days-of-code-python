import tkinter as tk

# Window
window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Button click function


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


# Label
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
new_button = tk.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = tk.Entry(width=10)
input.grid(column=3, row=2)

# Mainloop
window.mainloop()
