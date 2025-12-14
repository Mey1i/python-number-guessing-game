from art import logo 
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")
        return turns


def set_difficulty():
    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_mode == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print("Welcome to the Python Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

computer_choice = randint(1, 100)
turns = set_difficulty()

guess = 0

while guess != computer_choice and turns > 0:
    print(f"\nYou have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    turns = check_answer(guess, computer_choice, turns)

    if turns == 0:
        print("You've run out of guesses. You lose 😢")
        print(f"The number was {computer_choice}")
