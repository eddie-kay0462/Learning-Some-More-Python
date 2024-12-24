# This program compares two numbers input by the user
# It demonstrates different ways to compare numbers in Python using conditional statements

# Get two numbers from user input
x = int(input("What is x? "))
y = int(input("What is y? "))


# Method 1: Using if-elif-else to check less than, greater than, equal to
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")


# Method 2: Using logical OR operator to check inequality
# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# Method 3: Using not equal operator (!=)
# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# Method 4: Using equality operator (==)
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
