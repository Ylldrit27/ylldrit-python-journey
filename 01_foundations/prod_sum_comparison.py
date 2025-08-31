# Ask the user to input two numbers
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Compute sum
total = num1 + num2
print(f"Sum: {total}")

# Compute product
prod = num1 * num2
print(f"Product: {prod}")

# Compare numbers
if (num1 > num2):
    print(f"{num1} > {num2}, hence first number is greater")
elif (num2 > num1):
    print(f"{num2} > {num1}, hence second number is greater")
else:
    print('Both numbers are equal')

# Compare results
if (total > prod):
    print(f"{total} > {prod}, hence sum is greater")
elif (prod > total):
    print(f"{prod} > {total}, hence prod is greater")
else:
    print('Both results are equal')
