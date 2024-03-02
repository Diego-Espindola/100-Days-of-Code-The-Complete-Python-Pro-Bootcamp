import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Capstone")
screen.tracer(0)


def trace_heading(turtle, _difficulty):
    # Starts to listen the keys
    screen.listen()
    screen.onkeypress(turtle.up_walk, "Up")
    if _difficulty == 'easy':
        screen.onkeypress(turtle.down_walk, "Down")
        screen.onkeypress(turtle.r_walk, "Right")
        screen.onkeypress(turtle.l_walk, "Left")


def next_round(_player, _scoreboard, _car_manager):
    """Updates the level, show the congratulations message and then start the next round"""
    _car_manager.next_game()
    _player.next_game()
    _player.hideturtle()
    _scoreboard.next_game()
    screen.update()
    time.sleep(2)

    _player.showturtle()
    _car_manager.start_game()
    _scoreboard.update_score()
    screen.update()


def main():
    time_car = 0.3
    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()
    while True:
        difficulty = screen.textinput("Choose a difficulty", "To control all directions type 'easy', "
                                                             "or 'hard' to only go forward")
        if difficulty == 'easy':
            trace_heading(player, difficulty)
            break
        elif difficulty == 'hard':
            trace_heading(player, difficulty)
            break

    car_manager.start_game()
    game_is_on = True
    time_to_new_car = 0
    while game_is_on:
        time.sleep(0.1)
        time_to_new_car += time_car
        if not car_manager.created_car:
            car_manager.create_car()
        if time_to_new_car > 0.9:
            time_to_new_car = 0
            car_manager.created_car = False

        car_manager.move()
        if car_manager.car_crash(player):
            car_manager.clean_cars()
            player.hideturtle()
            scoreboard.end_game()
            game_is_on = False
        elif player.ycor() == 280:
            next_round(player, scoreboard, car_manager)
            time_car += 0.1
        screen.update()


if __name__ == "__main__":
    main()
    screen.exitonclick()
