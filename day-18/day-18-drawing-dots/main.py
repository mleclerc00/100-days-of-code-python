### This code will not work in repl.it as there is no access to the colorgram package here.###
## We talk about this in the video tutorials##
import colorgram
import random
import turtle as t


screen = t.Screen()
screen.setworldcoordinates(0, 0, 500, 500)
t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()

rgb_colors: list[colorgram.colorgram.Rgb] = []
colors: list[colorgram.Color] = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


def random_color():
    return random.choice(rgb_colors)


def dots(step: int, dot_size: int):
    for _ in range(0, 11):
        timmy.dot(dot_size, random_color())
        timmy.forward(step)
    timmy.setx(0)


timmy_height = 0
for _ in range(0, 11):
    dots(50, 20)
    timmy_height += 50
    timmy.sety(timmy_height)


screen.exitonclick()
