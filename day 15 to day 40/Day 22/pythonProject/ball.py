from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_way = 10
        self.x_way = 10

    def bounce(self):
        if self.xcor() == 380:
            self.x_way = -10
        if self.ycor() == 280:
            self.y_way = -10
        if self.xcor() == -380:
            self.x_way = 10
        if self.ycor() == -280:
            self.y_way = 10
        self.move()

    def start_moving(self):
        if -380 < self.xcor() < 380 and -280 < self.ycor() < 280:
            self.move()
        else:
            self.bounce()

    def move(self):
        self.goto(self.xcor() + self.x_way, self.ycor() + self.y_way)
# x goes right and left
