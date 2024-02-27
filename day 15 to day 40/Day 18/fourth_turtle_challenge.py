# Make the turtle do a random walk with random colors, with the same distance for each
# Make it thinner and faster
import time
from turtle import Turtle, Screen
import random as r
LIST_OF_COLORS = [(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)) for _ in range(100)]
LIST_OF_DEGREES = [90, 180, 270, 360]


def random_walk(turtle_object):

    turtle_object.pencolor(r.choice(LIST_OF_COLORS))
    direction = r.choice(LIST_OF_DEGREES)
    turtle_object.setheading(direction)
    turtle_object.forward(15)


screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(7)
turtle.pensize(3)
for _ in range(200):
    random_walk(turtle)
screen.exitonclick()
