# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

# Number of guesses given the level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty(difficulty: str) -> int:
    """Evaluates difficulty and returns the number of available guesses

    Args:
        difficulty (str): level of difficulty

    Returns:
        int: number of guesses allowed
    """
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS


def check_guess(user_guess: int, answer: int, turns: int) -> int:
    """Compares the users guess against the chosen random number

    Args:
        user_guess (int): users guess
        answer (int): chosen random number

    Returns:
        int: number of turns remaining
    """
    if user_guess > answer:
        print("Too high.")
    elif user_guess < answer:
        print("Too low.")
    else:
        print(f"You got it, the answer was {answer}")

    return turns - 1


def number_game() -> None:
    """Run the number game"""

    print(
        f"""
        {logo}
        Welcome to the number guessing game!
        I'm thinking of a number between 1 and 100.
        """
    )

    # Choose random number, set difficulty
    answer = randint(1, 100)
    number_of_guesses = set_difficulty(
        input("Choose a difficulty. Type 'easy' or 'hard': ")
    )

    # Use guess to control while loop
    guess = 0

    while guess != answer:
        print(f"You have {number_of_guesses} attempts remaining to guess the number.")
        # Make guess, check if its correct, subtract from remaining guesses
        guess = int(input("Make a guess: "))
        number_of_guesses = check_guess(guess, answer, number_of_guesses)

        # If no guesses remain, and not game over
        if number_of_guesses == 0:
            print("You've run out of guesses, you lose")
            print(f"The number was {answer}")
            return
        elif guess != answer:
            print("Guess again.")


number_game()
