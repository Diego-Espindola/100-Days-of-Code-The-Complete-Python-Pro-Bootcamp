"""
Instructions
💪 This is a difficult challenge! 💪
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
"""

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

true_sum = 0
love_sum = 0
for letter in name1+name2:
  if letter.upper() in "TRUE":
    true_sum += 1
  if letter.upper() in "LOVE":
    love_sum += 1

combined_numbers = int(str(true_sum) + str(love_sum))

if combined_numbers < 10 or combined_numbers > 90:
  print(f"Your score is {combined_numbers}, you go together like coke and mentos.")
elif combined_numbers <= 50 and combined_numbers >= 40:
  print(f"Your score is {combined_numbers}, you are alright together.")
else:
  print(f"Your score is {combined_numbers}.")
