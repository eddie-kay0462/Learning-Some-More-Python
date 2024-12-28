# print("#" * 10)
# print("#" * 10)
# print("#" * 10)
# print("#" * 10)
# print("#" * 10)
# print("#" * 10)
# print("#" * 10)
# print("#" * 10)
# print("#" * 10)
# print("#" * 10)


# for _ in range(4):
#     print("#")


def main():
    # print_column(3)
    print_square(4)

# def print_column(height):
#     for _ in range(height):
#         print("#")

#yet another way to do it
# def print_column(height):
#     print("#\n" * height, end="")

#print a row of question marks
def print_row(width):
    print("?" * width)

#print a square of question marks
def print_square(size):
    for _ in range(size):
        print_row(size)

main()

