import sys

#this is how to run the program in the terminal
#python name.py Edward. The sys.argv[1] is the first argument passed to the program
# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Usage: python name.py <name>")



#we could also use if and else to check if the user has passed a name
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1])

# full_name = sys.argv[1:]
# print("Hello, my name is", " ".join(full_name))

# print("Hello, my name is", sys.argv[1])



#it is sometimes useful to keep the error handling separate from the actual print statement. this is because the error handling is not part of the print statement
#As illustrated below. sys.exit() is used to exit the program if the user has not passed a name
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# print("Hello, my name is", sys.argv[1])


#this is how to print all the arguments passed to the program
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)



