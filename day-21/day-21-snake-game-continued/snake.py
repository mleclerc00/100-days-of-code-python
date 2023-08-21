from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
X_POSITION_START = 0
Y_POSITION_START = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """Create a snake from the Turtle class"""
        self.segments: list[Turtle] = []
        self.create()
        self.head: Turtle = self.segments[0]

    def create(self):
        """Generates multiple turtles in order to mimic a snake.  
            This also sets the starting position of each turtle and 
            adds each 'segment' of the snake to an array. 
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position: tuple[float, float]):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Iterates through each segment in the array to set a new position 
            for each segment will be the old position of the one it is following.
            Will also move the lead segment ahead by the MOVE_DISTANCE since it
            has no segment to follow.
        """
        for segment in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[segment - 1].pos()
            self.segments[segment].setposition(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Move the lead segment up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move the lead segment down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move the lead segment left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move the lead segment right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
