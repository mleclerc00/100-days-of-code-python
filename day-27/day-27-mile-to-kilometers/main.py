import tkinter as tk


window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Entry field
entry = tk.Entry(width=10)
entry.grid(column=1, row=0)

# Label Miles
label1 = tk.Label(text="Miles")
label1.grid(column=2, row=0)

# Label is equal to
label2 = tk.Label(text="is equal to")
label2.grid(column=0, row=1)

# Label answer
label3 = tk.Label(text="0")
label3.grid(column=1, row=1)

# Label Km
label4 = tk.Label(text="Km")
label4.grid(column=2, row=1)


def button_clicked():
    label3["text"] = round(float(entry.get()) * 1.609, 2)


# Button Calculate
button = tk.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# mainloop
window.mainloop()
