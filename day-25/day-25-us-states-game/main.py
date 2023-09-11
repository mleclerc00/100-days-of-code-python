import csv
import pandas
import turtle


ALIGNMENT = "left"
FONT = ("Arial", 12, "normal")

image = "./blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Name")
screen.addshape(image)

map = turtle.Turtle()
map.shape(image)

data = pandas.read_csv("./50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"Guess the state - {len(guessed_states)}/50", prompt="What's another state name?").title().strip()

    if answer_state == "Exit":
        break
    if answer_state in states:
        pen = turtle.Turtle()
        pen.penup()
        pen.hideturtle()
        current_state = data[data.state == answer_state]
        pen.goto(int(current_state.x), int(current_state.y))
        pen.write(answer_state, align="left", font=FONT)
        guessed_states.append(answer_state)

missing_states = pandas.DataFrame(list(set(states) - set(guessed_states)))
missing_states.to_csv("./states_to_learn.csv", header=False)
