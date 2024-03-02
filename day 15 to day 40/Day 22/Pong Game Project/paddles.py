from turtle import Turtle, ontimer

UP = 90
DOWN = 270
WIDTH = 5
HEIGHT = 1


class Paddles(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(WIDTH, HEIGHT, 0)
        self.goto(x_pos, y_pos)

    def move_up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
            #ontimer(self.move_downwards, 120)
