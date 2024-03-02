from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.draw_line()

    def draw_line(self):
        self.color("white")
        self.penup()


