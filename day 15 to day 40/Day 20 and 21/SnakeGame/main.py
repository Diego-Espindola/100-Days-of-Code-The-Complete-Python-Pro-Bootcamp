from turtle import Turtle, Screen
from snake import Snake
import time
import random

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
screen.bgcolor("Black")


def ate_fruit():
    r = random.randint(0, 20)
    return r == 1


snake = Snake()


def trace_heading():
    screen.listen()
    screen.onkey(snake.t_up, "Up")
    screen.onkey(snake.t_down, "Down")
    screen.onkey(snake.t_right, "Right")
    screen.onkey(snake.t_left, "Left")


def main():
    trace_heading()
    is_game_on = True
    while is_game_on:
        time.sleep(0.1)
        screen.update()
        snake.move()



if __name__ == "__main__":
    main()
    screen.exitonclick()
