"""
Instructions
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
"""

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
def year_to_week(year):
  return year*52


age = int(age)
max_human_age = 90
years_left = max_human_age - age

weeks_left = year_to_week(years_left)

print(f"You have {weeks_left} weeks left.")