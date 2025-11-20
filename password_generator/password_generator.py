import secrets
import string
import random

letters = string.ascii_letters   # Concatenation of lowercase and uppercase letters
digits = string.digits    # 0-9
special_chars = string.punctuation    # Special characters e.g. ;,!
selection_list = letters + digits + special_chars

# Ask the user to set password length
password_length = int(input("Please enter an integer to set password length: "))

while True:
    password = ""
    
    for i in range(password_length):
        password += "".join(secrets.choice(selection_list))
    
    # Constraint: at least 1 special character and at least 2 numbers
    if (any(char in special_chars for char in password) and 
        sum(char in digits for char in password) >= 2):
        break

print(password)