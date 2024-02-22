import random as r
from game_data import data
import art
import replit
LIST_OF_DATA = []

def pick_next_name():

  global LIST_OF_DATA
  range_limit = len(data) - 1
  random_number = r.choice([x for x in range(range_limit) if x not in LIST_OF_DATA])
  LIST_OF_DATA.append(random_number)
  return data[random_number]


def main():
  score = 0
  actual_name = pick_next_name()
  print(art.logo)
  while True:
    next_name = pick_next_name()
    print(f"Compare A: {actual_name['name']}, a {actual_name['description']}, from {actual_name['country']}")
    print(art.vs)
    print(f"Compare B: {next_name['name']}, a {next_name['description']}, from {next_name['country']}")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if actual_name['follower_count'] > next_name['follower_count']:
      winner_letter = 'A'
    else:
      winner_letter = 'B'

    if answer == winner_letter:
      actual_name = next_name
      score += 1
      replit.clear()
      print(art.logo)
      print(f"You're right! Current score: {score}.")
    else:
      replit.clear()
      print(art.logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      break

if __name__ == "__main__":
  main()
