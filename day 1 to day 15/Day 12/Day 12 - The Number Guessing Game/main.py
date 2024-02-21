import random as r
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def get_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
            if guess > 100 or guess < 0:
                raise ValueError
            return guess
        except ValueError:
            print("**Invalid input. Please enter a valid integer between 1 and 100.")

def get_difficulty():
    while True:
        try:
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
            if difficulty == "easy":
                return EASY_LEVEL_TURNS
            elif difficulty == "hard":
                return HARD_LEVEL_TURNS
            else:
                raise ValueError("**Invalid difficulty level. Please enter 'easy' or 'hard'.")
        except ValueError as e:
            print(e)


def check_attempt(number, guess):
    if guess == number:
        return True
    else:
        if guess > number:
            print("Too high")
        else:
            print("Too low")
        return False

def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number = r.randint(0, 100)
    attempts = get_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = get_guess()
        if check_attempt(number, guess):
            print(f"You got it! The answer was {number}.")
            return
        attempts -= 1

    print(f"You've run out of guesses! The answer was {number}.")

if __name__ == "__main__":
    main()
