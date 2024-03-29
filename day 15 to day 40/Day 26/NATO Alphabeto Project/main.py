# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd


# TODO 1. Create a dictionary in this format:
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
list_of_code_words = [nato_dict[letter.upper()] for letter in user_input]
print(list_of_code_words)
