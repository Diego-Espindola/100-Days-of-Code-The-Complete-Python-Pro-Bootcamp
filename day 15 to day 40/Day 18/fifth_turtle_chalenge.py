# make a spyrograph
# after that I made a different design with 51.42 degrees
import time
from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed(100)
screen = Screen()

keep_going = True
while keep_going:
    turtle.circle(100)
    turtle.left(51.42)
    if turtle.heading() == 0:
        keep_going = False

turtle.penup()
turtle.setposition((-900.0, 0.0))
screen.exitonclick()
