import random as r
from art import logo

def get_guess():
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

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
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 10 if difficulty == "easy" else 5

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
