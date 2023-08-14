from os import system
from art import logo

print(logo)
print("Welcome to the secret auction program.")

# Boolean for ending auction
more_bidders = True

# Create empty list for bids
bids = {}

# Find highest bidder
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount =  bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Start auction
while more_bidders is True:

    # Ask for user/bid
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))

    # Create dict and add to list
    bids[name] = price

    # Ask if there are more users and end if not
    more_bidders_prompt = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    # End auction if response is no
    if more_bidders_prompt == "no":
        more_bidders = False
        find_highest_bidder(bids)
    else:
        system('clear')
