from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.shape('blank')
        self.goto(-40, 250)
        self.increment_score()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)