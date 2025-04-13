from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(100, 270)
        self.write("score : {}".format(self.score), align="center", font=("Consolas", 20, "normal"))

    def plus_score(self):
        self.score += 1
        self.clear()
        self.write("score : {}".format(self.score), align="center", font=("Consolas", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Consolas", 20, "normal"))
