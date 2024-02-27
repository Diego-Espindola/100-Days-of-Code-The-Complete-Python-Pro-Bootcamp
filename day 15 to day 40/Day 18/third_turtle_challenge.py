# Draw a triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon, decagon with the same length on each the line
# make the line a different color for each

from turtle import Turtle, Screen
import random as r
LIST_OF_COLORS = [
    "AntiqueWhite1",
    "AntiqueWhite2",
    "AntiqueWhite3",
    "AntiqueWhite4",
    "agua",
    "aquamarine",
    "aquamarine1",
    "aquamarine2",
    "aquamarine3",
    "aquamarine4",
    "azure",
    "azure1",
    "azure2",
    "azure3",
    "azure4",
    "beige",
    "bisque",
    "bisque1",
    "bisque2",
    "bisque3",
    "bisque4",
    "black",
    "blanched almond",
    "BlanchedAlmond",
    "blue",
    "blue violet",
    "blue1",
    "blue2",
    "blue3",
    "blue4",
    "BlueViolet",
    "brown",
    "brown1",
    "brown2",
    "brown3",
    "brown4",
    "burlywood",
    "burlywood1",
    "burlywood2",
    "burlywood3",
    "burlywood4",
    "cadet blue",
    "CadetBlue",
    "CadetBlue1",
    "CadetBlue2",
    "CadetBlue3",
    "CadetBlue4",
    "chartreuse",
    "chartreuse1",
    "chartreuse2",
    "chartreuse3",
    "chartreuse4",
    "chocolate",
    "chocolate1",
    "chocolate2",
    "chocolate3",
    "chocolate4",
    "coral",
    "coral1",
    "coral2",
    "coral3",
    "coral4",
    "cornflower blue",
    "CornflowerBlue",
    "cornsilk",
    "cornsilk1",
    "cornsilk2",
    "cornsilk3",
    "cornsilk4",
    "crymson",
    "cyan",
    "cyan1",
    "cyan2",
    "cyan3",
    "cyan4",
    "dark blue",
    "dark cyan",
    "dark goldenrod",
    "dark gray",
    "dark green",
    "dark grey",
    "dark khaki",
    "dark magenta",
    "dark olive green",
    "dark orange",
    "dark orchid",
    "dark red",
    "dark salmon",
    "dark sea green",
    "dark slate blue",
    "dark slate gray",
    "dark slate grey",
    "dark turquoise",
    "dark violet",
    "DarkBlue",
    "DarkCyan",
    "DarkGoldenrod",
    "DarkGoldenrod1",
    "DarkGoldenrod2",
    "DarkGoldenrod3",
    "DarkGoldenrod4"
]


def draw_a_shape(def_sides, turtle_object):
    degrees = 360 / def_sides
    turtle_object.pencolor(r.choice(LIST_OF_COLORS))
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
