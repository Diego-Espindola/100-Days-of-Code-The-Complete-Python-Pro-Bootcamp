# Draw a dashed line

from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("BlueViolet")
turtle.pencolor("black")

for _ in range(50):
    turtle.forward(2)
    turtle.penup()
    turtle.forward(2)
    turtle.pendown()

screen = Screen()
screen.exitonclick()
