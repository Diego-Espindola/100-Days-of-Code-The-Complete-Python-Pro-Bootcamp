# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("Hello")
#   print("How are you doing?")
#   print("Isn't tje weather nice today?")

# greet()

# Function that allows for input

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How do you do {name}?")

# greet_with_name("Diego Espindola")

# Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

# Positional argument
greet_with("Diego Espindola", "Mexico")

# Keyword argument
greet_with(location = "Mexico", name = "Diego")