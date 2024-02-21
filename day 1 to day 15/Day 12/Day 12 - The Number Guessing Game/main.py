import random as r
from art import logo

NUMBER = r.randint(0,100)
GUESSED = False
def check_attempt(attempt):
    global attempts
    if attempt == NUMBER:
        return True
    else:
        attempts -= 1
        if attempt > NUMBER:
            print("Too high")
        else:
            print("Too low")
        return False

def main():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        attempts = 5
    else:
        attempts = 10

    while attempts > 0 and not GUESSED:
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempt = int(input("Make a guess: "))
        GUESSED = check_attempt(attempt)

    if(GUESSED):
        print(f"You got it! The answer was {NUMBER}.")
    else:
        print(f"You've run out of guesses! The answer was {NUMBER}.")

if __name__ == "__main__":
    main()