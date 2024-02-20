############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

## Trying it with zero hints
from replit import clear
from art import logo
import random

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}


def sum_cards(cards_value):
  if sum(cards_value) == 21 and len(cards_value) == 2:
    return 0

  if 11 in cards_value and sum(cards_value) > 21:
    for index, card in enumerate(cards_value):
      if card == 11 and sum(cards_value) > 21:
        cards_value[index] = 1

  return sum(cards_value)


def main():
  print(logo)
  cards_keys = list(cards.keys())
  player_cards = random.choices(cards_keys, k=2)
  computer_cards = random.choices(cards_keys, k=2)
  player_cards_values = []
  computer_cards_values = [cards[key] for key in computer_cards]
  blackJack = False
  while True:
    player_cards_values = [cards[key] for key in player_cards]
    player_sum = sum_cards(player_cards_values)

    print(
        f"\nYour cards: [ {' | '.join(player_cards)} ]. current score: {player_sum}"
    )
    if player_sum == 0:
      player_sum = 21
      blackJack = True
      break
    print(f"Computer's first card: {computer_cards[0]}")

    if player_sum == 21:
      break
    elif player_sum > 21:
      break

    if input('Type "y" to get another card, type "n" to pass: ') == 'n':
      break
    else:
      player_cards += random.choice(cards_keys)

  computer_sum = sum_cards(computer_cards_values)
  while computer_sum < 17:
    choice = random.choice(cards_keys)
    computer_cards_values.append(cards[choice])
    computer_cards.append(choice)
    computer_sum = sum_cards(computer_cards_values)

  print(
      f"\nYour final hand: [ {' | '.join(player_cards)} ]. final score: {player_sum}"
  )
  print(
      f"Computer's final hand: [ {' | '.join(computer_cards)} ]. final score: {computer_sum}"
  )
  win = True
  tie = False

  if player_sum > 21:
    win = False
  elif player_sum == 21:
    win = True
  elif computer_sum > player_sum:
    if computer_sum  > 21:
      win = True
    else:
      win = False
  elif computer_sum == player_sum:
    tie = True
    win = False

  if blackJack:
    print("You got a blackjack! You win!")
  elif win:
    print("You win")
  elif tie:
    print("It's a tie")
  else:
    print("You lose")


if __name__ == "__main__":
  while input(
      "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    main()