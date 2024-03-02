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
        self.moving_up = False
        self.moving_down = False

    def move_up(self):
        self.moving_up = True
        self.move_upwards()

    def stop_move_up(self):
        self.moving_up = False

    def move_down(self):
        self.moving_down = True
        self.move_downwards()

    def stop_move_down(self):
        self.moving_down = False

    def move_upwards(self):
        if self.moving_up and self.ycor() < 240:
            self.sety(self.ycor() + 20)
            ontimer(self.move_upwards, 120)

    def move_downwards(self):
        if self.moving_down and self.ycor() > -240:
            self.sety(self.ycor() - 20)
            ontimer(self.move_downwards, 120)
