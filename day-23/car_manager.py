from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.all_cars: list[Turtle] = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self) -> None:
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(choice(COLORS))
            new_car.setpos(310, self.random_y())
            self.all_cars.append(new_car)

    def move(self) -> None:
        for car in self.all_cars:
            car.backward(self.car_speed)

    def random_y(self) -> int:
        return randint(-250, 250)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
