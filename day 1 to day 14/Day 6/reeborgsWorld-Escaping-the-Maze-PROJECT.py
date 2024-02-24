# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    for x in range(0,3):
        turn_left()

count = 0
while not at_goal():
    if count == 4:
        if front_is_clear():
            count = 0
            move()
        else:
            while front_is_clear():
                move()
            turn_left()
    if right_is_clear():
        count += 1
        turn_right()
        move()
    elif front_is_clear():
        count = 0
        move()
    else:
        count = 0
        turn_left()
