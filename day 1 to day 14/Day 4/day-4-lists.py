# import random

# random_integer = random.randint(0, 4)
# random_float = random.random()

# random_high = random_integer + random_float
# print(random_high)

# ################################

# # Now, let's say that I want to store all of the names of the states of the US

# states_of_america = [
#     "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
#     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
#     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
#     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illiois",
#     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
#     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
#     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
#     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
#     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
# ]

# # print(states_of_america[-2])
# # https://docs.python.org/3/tutorial/datastructures.html
# states_of_america[1] = "Pencilvania"

# states_of_america.append("Diegoland")
# states_of_america.extend(["Angelaland", "Jack Bauer Land"])
# print(states_of_america)


#####################
# Nested lists

# https://www.delish.com/food-news/a26872638/dirty-dozen-foods-list-2019/
# dirty_dozen = [
#     "Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
#     "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"
# ]

fruits = [
    "Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
    "Pears"
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)