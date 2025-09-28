from random import randrange

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
number = randrange(100)


def compare(user_guess):
    if guess > number and attempts > 0:
        print("Too high.\nGuess again.")
    elif guess < number and attempts > 0:
        print("Too low.\nGuess again.")
    elif attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")
    else:
        print(f"You got it! The answer was {number}.")


easy_attempts = 10
hard_attempts = 5

if difficulty == "easy":
    attempts = easy_attempts
else:
    attempts = hard_attempts

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))
    attempts -= 1
    compare(guess)
    if guess == number:
        attempts = 0
