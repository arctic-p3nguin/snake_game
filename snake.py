from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # the first three segments' position
MOVE_DISTANCE = 20  # how far the segments move each time
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.first = self.segments[0]
        self.first.shape("square")

    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.color("green")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def create_snake(self):
        for position in STARTING_POSITIONS:  # create the snake
            self.add_segment(position)

    def extend(self):  # make the snake longer
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(1, len(self.segments)):  # move the snake (each segment follows the previous segment's position)
            pos = self.segments[-1 - i].pos()
            self.segments[-1 * i].goto(pos)
        self.first.forward(MOVE_DISTANCE)

    def up(self):  # change the snake's direction
        if self.first.heading() != DOWN:  # check if the snake's direction is opposite
            self.first.shape("square")
            self.first.setheading(UP)

    def down(self):
        if self.first.heading() != UP:
            self.first.shape("square")
            self.first.setheading(DOWN)

    def left(self):
        if self.first.heading() != RIGHT:
            self.first.shape("square")
            self.first.setheading(LEFT)

    def right(self):
        if self.first.heading() != LEFT:
            self.first.shape("square")
            self.first.setheading(RIGHT)
