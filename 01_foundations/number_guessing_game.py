import random

# Computer picks a random number between 1 and 10
secret = random.randint(1, 10)

# Ask the user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Insert a counter to track the number of guesses
count = 1

# Loop until they guess correctly
while guess != secret:
    if guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    count += 1
    guess = int(input("Guess again: "))

print("🎉 Correct! The secret number was", secret)
print(f"You guessed in {count} tries!")