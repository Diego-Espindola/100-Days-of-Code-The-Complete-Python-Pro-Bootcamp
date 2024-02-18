from art import logo
from replit import clear
#HINT: You can call clear() to clear the output in the console.

def main():

    print(logo)
    print("Welcome to the secret auction program.")
    other_bidders = True

    bidders = {}

    while other_bidders:
        name = input("What is your name?: ")
        bid = float(input("What's your bid?: $"))
        bidders[name] = bid

        have_next = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
        if have_next == "no":
            other_bidders = False
        clear()

    # Checks the highest bid
    highest_bid = 0
    winner = ""
    for key in bidders:
        if bidders[key] > highest_bid:
            highest_bid = bidders[key]
            winner = key

    print(f"The winner was {winner}. {highest_bid}")

if __name__== "__main__":
  main()