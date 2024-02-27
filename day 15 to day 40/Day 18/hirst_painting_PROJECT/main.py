# Create a spot paint
# Requirements
# You're going to paint a painting with 10 by 10 rows of spots
# Each of the dots should be 20 in size and spaced apart by around 50 paces
from get_painting_colors import LIST_OF_COLORS
from turtle import Turtle, Screen
import random as r

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.penup()
turtle.setposition(x=-100, y=-100)
first_position = turtle.position()
for y in range(1, 11):
    for x in range(1, 11):
        color = r.choice(LIST_OF_COLORS)
        turtle.pendown()
        turtle.color(color)
        turtle.dot(size=20)

        turtle.penup()
        turtle.forward(30)

    x_position = first_position[0]
    new_y_position = turtle.position()[1] + 30
    turtle.setposition(x_position, y=new_y_position)


screen.exitonclick()
