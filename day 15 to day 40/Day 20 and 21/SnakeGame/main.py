from turtle import Turtle, Screen
import time

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
screen.bgcolor("Black")
HEADING = 0

FIRST_TURTLE = Turtle(shape="square")
FIRST_TURTLE.color("White")
FIRST_TURTLE.penup()


def t_left():
    FIRST_TURTLE.setheading(90)


def t_right():
    FIRST_TURTLE.setheading(270)


def t_forward():
    FIRST_TURTLE.setheading(0)


def t_backward():
    FIRST_TURTLE.setheading(180)


def trace_heading():
    screen.listen()
    screen.onkeypress(t_left, "Up")
    screen.onkeypress(t_right, "Down")
    screen.onkeypress(t_forward, "Right")
    screen.onkeypress(t_backward, "Left")


def initiate():
    x = 0
    turtles = [FIRST_TURTLE]
    for _ in range(2):
        x -= 20
        turtle = FIRST_TURTLE.clone()
        turtle.goto(x, 0)
        turtles.append(turtle)
    return turtles


def main():
    trace_heading()
    turtles = initiate()
    screen.update()

    is_game_on = True
    while is_game_on:
        time.sleep(0.2)
        previous_position = FIRST_TURTLE.position()
        FIRST_TURTLE.forward(20)
        for other_turtle in turtles[1:]:
            aux_position = other_turtle.position()
            other_turtle.goto(previous_position)
            previous_position = aux_position
        screen.update()


if __name__ == "__main__":
    main()
    screen.exitonclick()
