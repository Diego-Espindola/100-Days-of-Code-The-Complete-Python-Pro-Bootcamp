import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()


def write_state(state, position_x, position_y, _turtle):
    _turtle.goto(position_x, position_y)
    _turtle.write(arg=state, align='center', font=("Arial", 8, "normal"))


data_states = pd.read_csv("50_states.csv")
missing_states = data_states.state.to_list()
correct_guesses = 0
game_is_on = True
title = "Guess the state"
while game_is_on:
    answer = turtle.textinput(f"{title}", "What's another state's name?")
    line = data_states[data_states["state"] == answer.title()]
    if not line.empty:
        state_name = line["state"].item()
        x_coordinate = int(line["x"].item())
        y_coordinate = int(line["y"].item())

        # Update the counter and display the state
        correct_guesses += 1
        write_state(state_name, x_coordinate, y_coordinate, turtle_writer)
        if state_name in missing_states:
            missing_states.remove(state_name)

    if answer.lower() == "exit":
        game_is_on = False
        turtle_writer.goto(0, 0)
        turtle_writer.write("Congratulations! "
                            f"You've guessed {correct_guesses} states!\n"
                            f"Your not guessed states will be on the csv", align='center', font=("Arial", 16, "bold"))
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
    elif correct_guesses == len(data_states):
        game_is_on = False
        turtle_writer.goto(0, 0)
        turtle_writer.write("Congratulations! "
                            "You've guessed all states!", align='center', font=("Arial", 16, "bold"))

    title = f"{correct_guesses}/{len(data_states)} States Correct"

screen.exitonclick()
