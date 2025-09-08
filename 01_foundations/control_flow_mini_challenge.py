# Ask the user to input their test score
score = int(input("Enter your score: "))

# Identify the grade
if score >= 90 and score <= 100:
    print(f"Grade: A*")
elif score >= 80 and score <= 89:
    print(f"Grade: A")
elif score >= 70 and score <= 79:
    print(f"Grade: B")
elif score >= 60 and score <= 69:
    print(f"Grade: C")
elif score >= 50 and score <= 59:
    print(f"Grade: D")
elif score >= 40 and score <= 49:
    print(f"Grade: E")
elif score >= 0 and score <= 39:
    print(f"Grade: F")
else:
    print(f"Invalid score. Please enter between 0-100.")