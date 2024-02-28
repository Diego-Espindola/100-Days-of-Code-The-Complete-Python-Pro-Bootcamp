from turtle import Turtle, Screen
import random as r

GAME_RESULT = ""


def create_map():
    turtle_designer = Turtle()
    turtle_designer.hideturtle()
    turtle_designer.speed(100)
    turtle_designer.penup()
    turtle_designer.setposition(x=250, y=-110)

    turtle_designer.pendown()
    turtle_designer.left(90)
    for _ in range(25):
        if _ % 2 == 0:
            turtle_designer.forward(10)
        else:
            turtle_designer.penup()
            turtle_designer.forward(10)
            turtle_designer.pendown()


def position_turtles(y=-110):
    new_turtles = []
    colors = ['purple', 'yellow', 'red', 'green', 'blue', 'orange']
    for color in colors:
        y += 30
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.setposition(x=-240, y=-y)
        new_turtles.append(new_turtle)
    return new_turtles


def check_the_winner(list_of_turtles):
    position = 0
    draw_turtles = []
    for check_turtle in list_of_turtles:
        new_position = check_turtle.position()[0]
        if new_position > position:
            position = new_position
            winner = check_turtle
            one_winner = True
        elif new_position == position and position != 0:
            draw_turtles.append(check_turtle.pencolor())
            one_winner = False

    if one_winner:
        return winner.pencolor()
    else:
        return draw_turtles


def main():
    global GAME_RESULT
    turtles = position_turtles()
    game_has_stop = False
    while not game_has_stop:
        turtles_in_the_final_line = []
        for turtle in turtles:
            paces = r.randint(0, 10)
            turtle.forward(paces)
            if turtle.position()[0] >= 230:
                turtles_in_the_final_line.append(turtle)

        if len(turtles_in_the_final_line) > 0:
            result = check_the_winner(turtles_in_the_final_line)
            if type(result) is str:
                if result == user_bet:
                    GAME_RESULT = f"You won the bet, {result.capitalize()} turtle has won, congratulations!"
                else:
                    GAME_RESULT = f"You lose, {result.capitalize()} turtle has won, try again next time!"
            else:
                GAME_RESULT = f"It was a draw, the turtles that come to the end were:\n {', '.join(result)}"
            game_has_stop = True


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?"
                                                              " Chose a color: 'purple','yellow','red',"
                                                              "'green','blue','orange'")
    while user_bet and user_bet != "finish":
        screen.clear()
        create_map()
        main()
        user_bet = screen.textinput(title=GAME_RESULT, prompt="If you want to try again, select a color:\n"
                                                              "'purple','yellow','red','green','blue','orange'\n"
                                                              "Else you can type 'finish' to end the bets")
