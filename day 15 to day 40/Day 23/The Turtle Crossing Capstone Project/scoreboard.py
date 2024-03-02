from turtle import Turtle

FONT = ("Courier", 24, "normal")
CONGRATULATIONS_FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-220, y=265)
        self.write(arg=f"Level: {self.level}", align='left', font=FONT)

    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align='center', font=FONT)
        self.goto(x=0, y=-40)
        self.write(arg=f"You reached level {self.level}", align='center', font=FONT)

    def congratulations(self):
        self.clear()
        self.goto(x=0, y=80)
        self.write(arg=f"Congratulations, you've reached level: {self.level}", align='center', font=CONGRATULATIONS_FONT)

    def next_game(self):
        self.level += 1
        self.congratulations()
