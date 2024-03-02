from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Pong")
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.tracer(n=0)


def trace_keyboard(p_1, p_2):
    screen.listen()
    screen.onkeypress(p_1.move_up, "Up")
    screen.onkeypress(p_1.move_down, "Down")

    screen.onkeypress(p_2.move_up, "w")
    screen.onkeypress(p_2.move_down, "s")


scoreboard = Scoreboard()
r_paddle = Paddles(x_pos=350, y_pos=0)
l_paddle = Paddles(x_pos=-350, y_pos=0)
trace_keyboard(r_paddle, l_paddle)
ball = Ball()
game_is_on = True
while game_is_on:
    ball.start_moving()
    time.sleep(ball.time_sleep)
    # Detect collision with paddle
    if (ball.distance(r_paddle) < 80 or ball.distance(l_paddle) < 80) and ball.xcor() in [330, -330]:
        ball.touch_paddle()

    if ball.paddle_miss():
        if ball.side == "left":
            scoreboard.r_point()
        else:
            scoreboard.l_point()
        ball.reset_ball()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_is_on = False
        ball.hideturtle()
        scoreboard.end_game()
    screen.update()

screen.exitonclick()
