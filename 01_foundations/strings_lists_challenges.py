"""
1. Create a string with your full name. Print:

    a) Your first character
    b) Your last character
    c) The length of the string

"""

name = "Ylldrit Miftari"

print(name[0])  # Y

print(name[-1])  # i

print(len(name))  # 15

"""
2. Create a list of your 5 favourite movies. Then:

    a) Add another movie at the end
    b) Remove one movie
    c) Print the final list
"""

movies = ["Spiderman", "Kung Fu Panda", "Madagascar", "Big Hero 6", "Zootopia", "Deadpool"]

movies.append("Thor")
movies.remove("Zootopia")
print(movies)