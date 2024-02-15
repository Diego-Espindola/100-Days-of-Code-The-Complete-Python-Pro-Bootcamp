#Step 1
import random as r

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = r.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
got_right = False

for index, letter in enumerate(random_word):
    if (letter == guess):
        random_word[index] == guess
        got_right = True
if(got_right):
  print("Good guess")