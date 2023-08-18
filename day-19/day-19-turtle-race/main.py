from turtle import Turtle, Screen
from random import randint

width: int = 500
height: int = 400
colors: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles: list[Turtle] = []
screen = Screen()
screen.setup(width, height)

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color: {colors} ")


def starting_position(offset: int):
    x_postion: float = -(width / 2 - 20)
    y_postion: float = (height / 2) - (offset * 55)
    return (x_postion, y_postion)


count = 1
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(starting_position(count))
    count += 1
    all_turtles.append(turtle)


if user_bet:
    is_race_on: bool = True
else:
    exit()

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(randint(0, 5))
        if turtle.xcor() == (width / 2 - 60):
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winning color")
            else:
                print(f"You've lost. The {turtle.pencolor()} turtle is the winning color")

screen.exitonclick()
