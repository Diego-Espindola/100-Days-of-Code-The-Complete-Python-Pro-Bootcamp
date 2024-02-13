import threading
import time

treasure_box = '''
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
                                       
                                       
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''' 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
##################################


class WrongPlaceError(Exception):
  pass

def check_place(place, correct_way, trap):
  if place.lower() == correct_way:
    #pass
  else:
    # Raise an exception to halt the code execution
    raise WrongPlaceError(trap)

# Function to simulate the treasure hunting game
def treasure_hunt():
  # Simulate the journey
  print(treasure_box)
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.")
  
  check_place(input("\nYou're on your adventure! You reach a crossroad, which way do you go? 'left' or 'right'\n"), 'left', '\nYou\'ve reached the wrong place and encountered a hungry lion. Game over!')
  print("You got it right, congratulations!! Let's continue.")
  check_place(input("\nOn your way to the treasure you can go swimming through the lake or walking through the forest, which way do you go? 'swim' or 'walk'\n"), 'swim', '\nYou were attacked by vespas and died. Game over!')
  print("You are going through the right place, we're almost at the treasure room, keep swimming")
  choice = input("\nYou've reached the treasure room, but there are three doors in front of you, which one do you choose? 'red', 'blue' or 'yellow'\n").lower()
  if(choice == "red"):
    trap = "\nYou've been burned by fire. Game over!"
  else:
    trap = "\nYou've been eaten by beasts. Game over!"
  
  check_place(choice, 'yellow', trap)

  print("\n\nYou've found the treasure! Congratulations!")

# Main function to start the game
def main():
  try:
      # Start the treasure hunting game
      treasure_hunt()
  except WrongPlaceError as e:
      print(e)  # Print the custom error message
      print("Better luck next time!")

if __name__ == "__main__":
  main()
