# Challenge 1: Print numbers 1 to 10 using a for loop

for i in range(1, 11):
    print(i)

# Challenge 2: Print all even numbers from 2 to 20

for i in range(2, 21, 2):
    print(i)

# Challenge 3: Write a while loop that keeps asking the user for a number until they enter 0

num = int(input("Enter a number (0 to quit): "))

while (num != 0):
    print(f"You entered {num}")
    num = int(input("Enter a number (0 to quit): "))

print("Loop ended. Goodbye!")