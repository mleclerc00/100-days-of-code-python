from turtle import Turtle, Screen, colormode
from random import randint, choice, random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("MediumAquamarine")

colormode(255)


def random_color():
    rgb = (randint(0, 255),
           randint(0, 255),
           randint(0, 255))
    return rgb


# Draw a square
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


# Draw a dashed line
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


# Drawing different shapes
def draw_shape(num_sides: int):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_num in range(3, 11):
    timmy.pencolor(random_color())
    draw_shape(shape_side_num)


# Draw a random walk
direction = [0, 90, 180, 270]
timmy.speed("fastest")
timmy.pensize(15)
for _ in range(300):
    timmy.pencolor(random_color())
    timmy.setheading(choice(direction))
    timmy.forward(25)

# Draw a spirograph


def draw_spirograph(size_of_gap: int):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


timmy.speed("fastest")
draw_spirograph(3)

screen = Screen()
screen.exitonclick()
