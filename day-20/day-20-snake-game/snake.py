from turtle import Turtle

MOVE_DISTANCE = 20
X_POSITION_START = 0
Y_POSITION_START = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, shape: str, color: str, length: int):
        self.shape = shape
        self.color = color
        self.length = length
        self.segments: list[Turtle] = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for index in range(self.length):
            x_pos_segment_offset = -(index * 20)
            segment = Turtle(shape=self.shape)
            segment.penup()
            segment.color(self.color)
            segment.setposition((X_POSITION_START + x_pos_segment_offset), Y_POSITION_START)
            self.segments.append(segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[segment - 1].pos()
            self.segments[segment].setposition(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
