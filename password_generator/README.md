# 🔐 Project: Random Password Generator
This project is a simple but powerful random password generator written in Python.
It creates secure passwords containing:
* Uppercase letters
* Lowercase letters
* Digits
* Special characters

The program ensures that every generated password meets minimum security requirements, making it suitable for learning about randomness, security, and string manipulation.

## 🧠 What This Project Demonstrates
This project showcases my understanding of:
* Using Python’s `secrets` module for cryptographically secure randomness
* String handling with the `string` module
* Loops and conditional logic
* Validating constraints on generated output
* User input and error handling fundamentals

## ⚙️ How the Program Works
1. The user enters a desired password length.
2. The program randomly selects characters from:
    * `string.ascii_letters` (A–Z, a–z)
    * `string.digits` (0–9)
    * `string.punctuation` (special characters)
3. A password is generated using `secrets.choice()` for strong randomness.
4. The program checks that the password contains:
    * **At least 1 special character**
    * **At least 2 digits**
5. If the constraints are not met, a new password is generated until valid.

## ▶️ How to Run
Make sure you have Python installed, then run:

`py password_generator.py`

You will be prompted to enter the password length, and the program will output a secure generated password.

## 🧩 Key Parts of the Code

* **Character pool creation**:

    `selection_list = letters + digits + special_chars`


* **Secure random choice**:

    `secrets.choice(selection_list)`


* **Constraint validation**:

    `any(char in special_chars for char in password)` <br>
    `sum(char in digits for char in password) >= 2`

## 📚 Source Acknowledgement
The structure and concept of this project were based on the following tutorial:

> [*Create Random Password Generator Program Using Python*](https://www.codingal.com/coding-for-kids/blog/create-random-password-generator-program-using-python/#1) <br> by Sumit Singh, on Codingal

I adapted it for my own learning, expanding and modifying parts of the logic.

## 🚀 Possible Future Improvements
Here are ideas to expand this project in the future:
* Add strength levels (e.g., weak / medium / strong)
* Allow the user to toggle character sets (include/exclude symbols, numbers, etc.)
* Save generated passwords to a file
* Create a Tkinter GUI version
* Add a “regenerate” option