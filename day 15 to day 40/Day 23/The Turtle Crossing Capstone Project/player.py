from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Manages player movement and provides a foundation for controlling the player turtle in the game.
    """
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

    def up_walk(self):
        if self.ycor() < 280:
            self.setheading(90)
            self.forward(MOVE_DISTANCE)

    def l_walk(self):
        if self.xcor() > -280:
            self.setheading(180)
            self.forward(MOVE_DISTANCE)

    def r_walk(self):
        if self.xcor() < 280:
            self.setheading(0)
            self.forward(MOVE_DISTANCE)

    def down_walk(self):
        if self.ycor() > -280:
            self.setheading(270)
            self.forward(MOVE_DISTANCE)

    def next_game(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
