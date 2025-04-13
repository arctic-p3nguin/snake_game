from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from timer import Timer
import pygame

# set up sound effects
pygame.mixer.init()
bg_music = pygame.mixer.Sound("Happy.mp3")
eat = pygame.mixer.Sound("bite.mp3")
game_end = pygame.mixer.Sound("end.mp3")

# set up the screen
screen = Screen()
screen.bgpic("BG.png")
screen.setup(600, 600)
screen.title("Snake")
bg_music.play()

screen.tracer(0)  # turn off the animation

snake = Snake()  # create the snake
food = Food()  # generate the food
scoreboard = Scoreboard()  # present the scoreboard on the screen
timer = Timer() # set up the timer

# control the snake by pressing the arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True  # game start

while game_is_on:
    # update the screen every 0.1 second
    screen.update()
    time.sleep(0.1)

    snake.move()  # move the snake

    timer.countdown()  # counting down the time

    # detect the collision with food
    if snake.head.distance(food) < 15:
        eat.play()
        food.refresh()
        snake.extend()
        scoreboard.plus_score()

    # detect the collision with the wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        game_end.play()
        bg_music.stop()
        scoreboard.game_over()

    # detect the collision with the snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            game_end.play()
            bg_music.stop()
            scoreboard.game_over()

    # if the time has elapsed then game over
    if timer.remaining_time == 0:
        game_is_on = False
        game_end.play()
        bg_music.stop()
        scoreboard.game_over()

screen.exitonclick()
