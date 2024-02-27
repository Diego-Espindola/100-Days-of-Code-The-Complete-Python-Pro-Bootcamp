# Make the turtle do a random walk with random colors, with the same distance for each
# Change the pen size and make the turtle faster
import time
from turtle import Turtle, Screen
import random as r

LIST_OF_DEGREES = [90, 180, 270, 360]


def get_random_color():
    return (r.randint(0, 255) for _ in range(3))


def random_walk(turtle_object):
    turtle_object.pencolor(get_random_color())
    direction = r.choice(LIST_OF_DEGREES)
    turtle_object.setheading(direction)
    turtle_object.forward(10)


screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(7)
turtle.pensize(5)
for _ in range(200):
    random_walk(turtle)
screen.exitonclick()
