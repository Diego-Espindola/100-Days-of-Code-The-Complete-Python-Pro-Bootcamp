# Putting on practice oriented-object programming

# import time
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkOliveGreen4")
#
#
# my_screen = Screen()
# # print(my_screen.canvheight)
# time.sleep(3)
# timmy.forward(100)
# my_screen.exitonclick()

##############################################

from prettytable import PrettyTable

table = PrettyTable()
pokemons = [
    {"name": "Pikachu", "type": "Eletric"},
    {"name": "Squirtle", "type": "Water"},
    {"name": "Charmander", "type": "Fire"}
]

table.add_column("Pokemon Name", [pokemon['name'] for pokemon in pokemons])
table.add_column("Type", [pokemon['type'] for pokemon in pokemons])
table.align = "l"
print(table)


