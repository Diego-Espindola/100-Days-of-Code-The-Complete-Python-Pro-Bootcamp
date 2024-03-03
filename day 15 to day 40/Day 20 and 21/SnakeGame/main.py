from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("Black")


snake = Snake()
food = Food()
score_board = ScoreBoard()


def trace_heading():
    screen.listen()
    screen.onkeypress(snake.t_up, "Up")
    screen.onkeypress(snake.t_down, "Down")
    screen.onkeypress(snake.t_right, "Right")
    screen.onkeypress(snake.t_left, "Left")


def reset_game():
    score_board.reset()
    snake.reset()


def main():
    game_on = True
    trace_heading()
    while game_on:
        start_time = time.time()
        time.sleep(snake.delay)
        screen.update()
        if snake.line_moving:
            snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.eat_fruit()
            snake.extend()
            score_board.increment_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            reset_game()

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                reset_game()

        # Calculates the time spent in the loop and updates the delay
        end_time = time.time()  # End time of the loop
        loop_time = end_time - start_time  # Time spent in the loop
        snake.update_delay(loop_time)
        snake.line_moving = True
        snake.reset_delay_and_move_count()


if __name__ == "__main__":
    main()
    screen.exitonclick()
