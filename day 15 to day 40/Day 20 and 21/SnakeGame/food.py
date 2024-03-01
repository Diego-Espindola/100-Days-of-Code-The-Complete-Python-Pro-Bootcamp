import random as r
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = r.randint(-265 // 15, 265 // 15) * 15
        random_y = r.randint(-265 // 15, 265 // 15) * 15
        self.goto(random_x, random_y)

    def eat_fruit(self):
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)


