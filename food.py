from turtle import Turtle, Screen
import random

FOOD_1 = "1.gif"
FOOD_2 = "2.gif"
FOOD_3 = "3.gif"
FOOD_4 = "4.gif"
FOOD_5 = "5.gif"
Screen().addshape(FOOD_1)
Screen().addshape(FOOD_2)
Screen().addshape(FOOD_3)
Screen().addshape(FOOD_4)
Screen().addshape(FOOD_5)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.shape(random.choice([FOOD_1, FOOD_2, FOOD_3, FOOD_4, FOOD_5]))
        self.goto(random_x, random_y)
