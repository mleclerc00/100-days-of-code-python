from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """Creates scoreboard turtle to keep track of the score"""
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))

    def increment_score(self):
        """Increment the score every time the snake eats food"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=(FONT))
