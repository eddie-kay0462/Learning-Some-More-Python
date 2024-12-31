# try:
#     x = input("What's x? ")
#     int_x = int(x)
#     print(f"x is {int_x}")
# except ValueError:
#     print(f"{x} is not an integer")

"""
Try and except are used to handle errors in Python. Both try and except blocks share the same scope. This is because the code in the try block is executed first, and if an error occurs, the code in the except block is executed.
"""


#The code below is a more efficient way to handle errors. It uses the try and except blocks to handle errors, and the else block to execute the code outside the try and except blocks.
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         print(f"x is {x}")
#         break

#another version of the above code
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")



#using a function to handle errors
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")

# x = get_int()
# print(f"x is {x}")


#instead of printing the error message we can use pass to ignore the error, as shown below
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             pass

# x = get_int()
# print(f"x is {x}")



#IN the code below, the main function is used to get the input from the user, and the get_int function is used to handle the error.
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
