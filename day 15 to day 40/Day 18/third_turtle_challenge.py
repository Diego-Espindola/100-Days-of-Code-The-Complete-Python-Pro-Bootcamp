# Draw a triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon, decagon with the same length on each the line

from turtle import Turtle, Screen


def draw_a_shape(def_sides, turtle_object):
    degrees = 360 / def_sides
    for _ in range(def_sides):
        turtle_object.forward(100)
        turtle_object.right(degrees)


turtle = Turtle()
turtle.shape("turtle")
turtle.color("black", "BlueViolet")
for sides in range(3, 11):
    draw_a_shape(sides, turtle)
screen = Screen()
screen.exitonclick()
