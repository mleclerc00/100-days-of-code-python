import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player: Player = Player()
car_manager: CarManager = CarManager()
scoreboard: Scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    car_manager.create_car()
    car_manager.move()

    time.sleep(0.1)
    screen.update()

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
