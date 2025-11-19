import random

lower_bound = 1
upper_bound = 100
max_attempts = 10

# Generate a random number within the upper and lower bounds
secret_number = random.randint(lower_bound, upper_bound)

def get_guess():
    """
    A function that continuously prompts the user to enter a number - within
    the specified range - until they provide a valid input.
    """
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, secret_number):
    """
    A function that takes the user's guess and the secret number as
    inputs and provides feedback on whether the guess is correct,
    too high, or too low.
    """
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"
    
def play_game():
    """A function that handles the game logic"""
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print(f"Congratulations! You guessed the secret number {secret_number}" 
                  + f" in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again!")
            print(f"You have {remaining_attempts} attempts left.")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")

# Call play_game() when program runs
if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()