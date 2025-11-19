# 🎯 Project: Number Guessing Game

This project is a simple interactive Python game where the player must guess a randomly generated number within a limited number of attempts.
It demonstrates core Python concepts such as:
* User input handling
* Loops and conditionals
* Functions and modular design
* Error handling with `try`/`except`
* Random number generation

This project is part of my **Python learning journey**.

## 🕹️ How the Game Works
1. The program randomly selects a number between **1 and 100**.
2. The player has **10 attempts** to guess the secret number.
3. After each guess, the program gives feedback:
    * **"Too high"**
    * **"Too low"**
    * **"Correct"**
4. If the player guesses correctly, the game ends and displays the number of attempts used.
5. If the player runs out of attempts, the game reveals the secret number.

## 📄 Features
✔ Input validation (handles non-numeric and out-of-range values) <br>
✔ Clear user feedback <br>
✔ Structured using functions (`get_guess`, `check_guess`, `play_game`) <br>
✔ Beginner-friendly logic <br>
✔ Clean, readable code

## ▶️ How to Run the Game

Make sure you have Python installed, then run:

`py guessing_game.py`

You will be prompted to enter guesses until you win or run out of attempts.

## 🧩 Code Structure
* `get_guess()`
    * Prompts the user until a valid number is entered.
* `check_guess(guess, secret_number)`
    * Compares the guess with the secret number and returns feedback.
* `play_game()`
    * Main game loop that handles attempts, tracking, and output messages.

## 📚 Source Acknowledgement
The structure and concept of this project were based on the following tutorial:

> [*"How to Code a Simple Number Guessing Game in Python"*](https://dev.to/balapriya/how-to-code-a-simple-number-guessing-game-in-python-4jai) <br>
by Bala Priya C, on DEV Community

I adapted and customised the code as part of my learning.

## 🚀 Possible Future Improvements
* Add difficulty levels (easy / medium / hard)
* Allow the user to choose the number range
* Add a replay option
* Add input timeout for extra challenge
* Convert to a GUI version (Tkinter or PyGame)