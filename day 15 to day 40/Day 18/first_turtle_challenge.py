# Draw a square
import time
from turtle import *

turtle = Turtle()
turtle.shape("turtle")
turtle.color("BlueViolet")

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

screen = Screen()
screen.exitonclick()
