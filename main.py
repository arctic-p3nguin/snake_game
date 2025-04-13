from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# set up the screen
screen = Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.title("Snake")

screen.tracer(0)  # turn off the animation

snake = Snake()  # create the snake
food = Food()  # generate the food
scoreboard = Scoreboard()  # present the scoreboard on the screen

# control the snake by pressing the arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True  # game start

while game:
    # update the screen every 0.1 second
    screen.update()
    time.sleep(0.1)

    snake.move()  # move the snake

    # detect the collision with food
    if snake.first.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.plus_score()

    # detect the collision with the wall
    if snake.first.xcor() > 300 or snake.first.xcor() < -300 or snake.first.ycor() > 300 or snake.first.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # detect the collision with the snake body
    for segment in snake.segments[1:]:
        if snake.first.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
