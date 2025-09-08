# A program to check if a number entered is positive, negative, or zero

# Input a number
num = int(input(f"Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")