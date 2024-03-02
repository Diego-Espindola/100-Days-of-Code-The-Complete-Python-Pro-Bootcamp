from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.draw_line()

    def draw_line(self):
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.goto(0, -350)
        self.setheading(90)
        for x in range(0, 65):
            if x % 2 == 0:
                self.pendown()
                self.forward(10)
            else:
                self.penup()
                self.forward(10)
        self.penup()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def end_game(self):
        self.update_scoreboard()
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        self.draw_line()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        self.draw_line()
