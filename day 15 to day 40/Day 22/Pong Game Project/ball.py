from turtle import Turtle

BALL_SPEED = 0.07


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_way = 10
        self.x_way = 10
        self.side = "right"
        self.time_sleep = BALL_SPEED

    def update_side(self):
        if self.x_way > 0:
            self.side = "right"
        else:
            self.side = "left"

    def bounce(self):
        if self.ycor() in [280, -280]:
            self.y_way *= -1

    def paddle_miss(self):
        return self.xcor() in [380, -380]

    def touch_paddle(self):
        self.x_way *= -1
        self.time_sleep *= 0.9

    def reset_ball(self):
        self.time_sleep = BALL_SPEED
        self.setposition(0, 0)
        self.x_way *= -1

    def start_moving(self):
        self.bounce()
        self.move()

    def move(self):
        self.goto(self.xcor() + self.x_way, self.ycor() + self.y_way)
        self.update_side()
# x goes right and left
