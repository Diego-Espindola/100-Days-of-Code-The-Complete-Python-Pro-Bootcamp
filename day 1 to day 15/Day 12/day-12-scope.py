################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# print(potion_strength) # NameError: not defined
# # You can only use it when you're inside the function
# # If u want it to be accessible outside the function, you have to use global scope

# # Global Scope
# player_health = 10
# def drink_potion():
#   potion_strength = 2
#   print(player_health)

# drink_potion()
# # Its a 'Namespace' that is valid at certain scopes


# # A function will be always avaible, unless it has been created inside a function, then it will have a local scope
# # E.g.
# def game():
#   def drink_potion():
#     potion_strength = 2 # Nested two levels deep
#     print(player_health)

#   drink_potion()
# drink_potion()# NameError

# Whenever you give a name to something, you need to pay attention to the scope of that name


# # There's no block scope

# if 3 > 2:
#   a_variable = 10 # it doesn't change the scope of the variable

# # E.g.
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#   new_enemy = enemies[0]

# print(new_enemy) # It works

# # Remember: if you create a variable within a function, then it's only available within that function, but if you create a variable within an if block or a while loop or a for loop, then that doesn't count as creatin a separate local scope


# # Modifying Global Scope

# enemies = 1

# def increase_enemies():
#   new_number_of_enemies = enemies + 1
#   return new_number_of_enemies 

# # Or u can use the global

# def increase_enemies():
#   global enemies
#   enemies += 1
#   print(f"enemies inside function: {enemies}")

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")


# # Global Constants
# # In order to differentiate these constants that you'll never change, you can turn them into all uppercase separated with underscores

# # Using uppercase letters and underscores for global constants doesn't change how the code functions; it's primarily for readability and maintainability. By following this convention, you make your code easier to understand for yourself and other developers who may read or work with your code in the future. It's a way of communicating the intent and significance of certain values within the codebase.

# PI = 3.14159
