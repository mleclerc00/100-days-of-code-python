from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        """Inherits from the Turtle class to create a food object for the snake to eat"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Generates random x,y coordinates and moves food object to that location"""
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
