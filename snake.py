from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # the first three segments' position
MOVE_DISTANCE = 20  # how far the segments move each time
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
UP_PIC = "S90.gif"
DOWN_PIC = "S270.gif"
LEFT_PIC = "S180.gif"
RIGHT_PIC = "S0.gif"
BODY = "6.gif"
Screen().addshape(UP_PIC)
Screen().addshape(DOWN_PIC)
Screen().addshape(LEFT_PIC)
Screen().addshape(RIGHT_PIC)
Screen().addshape(BODY)


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape(RIGHT_PIC)

    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.shape(BODY)
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
        self.head.forward(MOVE_DISTANCE)

    def up(self):  # change the snake's direction
        if self.head.heading() != DOWN:
            self.head.shape(UP_PIC)
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.shape(DOWN_PIC)
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.shape(LEFT_PIC)
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.shape(RIGHT_PIC)
            self.head.setheading(RIGHT)
