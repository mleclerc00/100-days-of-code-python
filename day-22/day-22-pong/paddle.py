from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
PADDLE_STEP = 20


class Paddle(Turtle):
    def __init__(self, x_position: int, y_position: int):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.create()

    def create(self):
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=PADDLE_HEIGHT, stretch_wid=PADDLE_WIDTH)
        self.goto(self.x_position, self.y_position)

    def up(self):
        new_y = self.ycor() + PADDLE_STEP
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - PADDLE_STEP
        self.sety(new_y)
