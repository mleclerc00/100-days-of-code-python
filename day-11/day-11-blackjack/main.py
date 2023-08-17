############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
from os import system

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(dealer_score, user_score):
    if user_score > 21:
        return "You went over, you lose"
    elif dealer_score == user_score:
        return "Draw"
    elif dealer_score == 0:
        return "Lose, dealer has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif dealer_score > 21:
        return "Dealer went over, you win"
    elif user_score > dealer_score:
        return "You win"
    else:
        return "You lose"

def blackjack():
    print(logo)
    user_cards = []
    dealer_cards = []
    is_game_over = False

    # deal 2 cards to user and dealer
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score < 17 and dealer_score != 0:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(dealer_score,user_score))

while input("Do you want to play a game of Blackjack? Yype 'y' or 'n': ") == "y":
    system('clear')
    blackjack()
