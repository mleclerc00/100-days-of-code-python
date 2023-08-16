# Higher lower game
# Given 2 items from the data list, user must pick which has more followers
# For each correct guess, user receives a point
# Option b becomes option a if the answer is correct
# Game ends when the user chooses the item with less followers
# http://www.higherlowergame.com/

from art import logo, vs
from game_data import data
from random import choice
from os import system


def format_data(account: dict) -> str:
    """Takes the account data and returns the printable format

    Args:
        account (dict): account dict

    Returns:
        str: formatted string for output
    """
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess: str, a_followers: int, b_followers: int) -> bool:
    """Take the user guess and follower counts and returns if they got it right

    Args:
        guess (str): users guess
        a_followers (int): account a follower count
        b_followers (int): account b follower count

    Returns:
        bool: True if guess is correct, otherwise False
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_over = False
    account_b = choice(data)

    while not game_over:
        account_a = account_b
        account_b = choice(data)
        while account_a == account_b:
            account_b = choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        system("clear")
        print(logo)
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


game()
