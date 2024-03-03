import random as r
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        # Ensure that the food appears in the middle of the screen
        random_x = r.randint(-12, 12) * 20 + 10  # Adjusted to match the snake's movement
        random_y = r.randint(-12, 12) * 20 + 10 # Adjusted to match the snake's movement
        self.goto(random_x, random_y)

    def eat_fruit(self):
        self.refresh()


