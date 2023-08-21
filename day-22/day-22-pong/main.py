from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

while True:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if (
        ball.distance(right_paddle) < 50 and ball.xcor() < 340
        or ball.distance(left_paddle) < 50 and ball.xcor() < -340
    ):
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_point()
