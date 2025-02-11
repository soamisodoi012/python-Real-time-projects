import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

    secret_number = random.randint(lower, upper)
    attempts = 0

    while True:
        guess = int(input(f"Guess a number between {lower} and {upper}: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
