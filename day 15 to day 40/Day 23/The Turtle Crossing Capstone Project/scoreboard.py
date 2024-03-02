from turtle import Turtle

FONT = ("Courier", 24, "normal")
CONGRATULATIONS_FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    """
    Implements methods to update and display the current game level, end the game with a "Game Over" message,
    and congratulate the player on reaching the next level.

    * Update Score: The update_score method clears the scoreboard and writes the current level at the specified position

    * End Game Message: The end_game method displays a "Game Over" message along with the level reached when
    the game ends.

    * Congratulations Message: The congratulations method clears the scoreboard and displays a
    congratulations message when the player reaches the next level.

    * Next Game Level: The next_game method increments
    the level and displays a congratulations message for reaching the next level.
    """
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
