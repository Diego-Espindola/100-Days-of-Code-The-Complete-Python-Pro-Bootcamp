from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
screen.bgcolor("Black")
HEADING = 0

FIRST_TURTLE = Turtle(shape="square")
FIRST_TURTLE.color("White")
FIRST_TURTLE.shapesize(stretch_wid=0.7, stretch_len=1, outline=5)
FIRST_TURTLE.penup()


def ate_fruit():
    r = random.randint(0,1)
    return r == 1


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
        time.sleep(1)
        #TODO save the last heading of each turtle, but in
        # first turtle we will have a problem about the person clicking and changing
        # I think, if the person clicks then I shouldn't change the heading,
        # but instead I should make a command to do something.
        # so, when it's pressed a Key more than one time, it saves the command
        previous_position = FIRST_TURTLE.position()
        FIRST_TURTLE.forward(20)
        for other_turtle in turtles[1:]:
            aux_position = other_turtle.position()
            # noinspection PyTypeChecker
            other_turtle.goto(previous_position)
            check_heading(other_turtle)
            previous_position = aux_position
        if ate_fruit():
            new_turtle = FIRST_TURTLE.clone()
            # noinspection PyTypeChecker
            new_turtle.goto(previous_position)
            turtles.append(new_turtle)

        screen.update()


if __name__ == "__main__":
    main()
    screen.exitonclick()
