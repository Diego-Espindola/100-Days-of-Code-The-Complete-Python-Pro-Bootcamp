from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.shape('blank')
        self.penup()
        self.goto(-40, 250)
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        self.high_score = self.score if self.score > self.high_score else self.high_score
        self.score = 0
        self.update_score()


        # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, align=ALIGNMENT, font=FONT)