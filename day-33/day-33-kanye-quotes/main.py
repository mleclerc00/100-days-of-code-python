from tkinter import Button, Canvas, PhotoImage, Tk

import requests


def get_quote():
    """Get a quote from the Kanye API and update the text on the canvas."""
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


# ---------------------------- UI SETUP ------------------------------- #

# Create and configure the window.
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create the canvas and add the background image and quote text.
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white"
)
canvas.grid(row=0, column=0)

# Create the button and add the Kanye image.
kanye_img = PhotoImage(file="./kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start the main loop.
window.mainloop()
