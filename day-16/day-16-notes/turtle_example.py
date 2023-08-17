# https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen


timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkSeaGreen")
timmy.forward(100)

screen = Screen()
print(screen.canvheight)
screen.exitonclick()
