import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = list("_" * len(chosen_word))
guessed_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letters:
        print(f"You've already guessed {guess}\n{' '.join(display)}")
        print(stages[lives])
        continue
    else:
        guessed_letters.append(guess)

    # Check guessed letter
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py.
    print(stages[lives])