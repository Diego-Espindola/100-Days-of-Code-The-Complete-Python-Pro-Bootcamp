rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

list_of_options = [rock, paper, scissors]

def checks_who_wins(player, computer):

  print(list_of_options[player])
  print("Computer chose:")
  print(list_of_options[computer])

  if player == computer:
    return "draw"

  strForm = ""
  list_shapes = [player, computer]
  list_shapes.sort(reverse=False)
  for shape in list_shapes:
    strForm += str(shape)
  # print(strForm)
  if strForm == "01":
    if player == 1:
      return "win"
  elif strForm == "02":
    if player == 0:
      return "win"
  elif strForm == "12":
    if player == 2:
      return "win"

  return "lose"



gamer_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)
if gamer_choice < 2 or gamer_choice < 0:

  result = checks_who_wins(gamer_choice, computer_choice)
  if result == "win":
    print("You win!")
  elif result == "draw":
    print("It's a draw")
  else:
    print("You lose")
else:
  print("You tiped an invalid number, you loose")
