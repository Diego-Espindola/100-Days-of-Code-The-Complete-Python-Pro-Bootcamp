from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
screen.bgcolor("Black")


GAME_ON = True
snake = Snake()
food = Food()
score_board = ScoreBoard()


def trace_heading():
    screen.listen()
    screen.onkey(snake.t_up, "Up")
    screen.onkey(snake.t_down, "Down")
    screen.onkey(snake.t_right, "Right")
    screen.onkey(snake.t_left, "Left")


def end_game():
    global GAME_ON
    GAME_ON = False
    score_board.game_over()


def main():
    global GAME_ON
    trace_heading()
    while GAME_ON:
        time.sleep(0.1)
        screen.update()
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.eat_fruit()
            snake.extend()
            score_board.increment_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            end_game()

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                end_game()


if __name__ == "__main__":
    main()
    screen.exitonclick()
