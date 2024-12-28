# First install tabulate using pip:
# pip install tabulate

from tabulate import tabulate
# students = ["Hermione", "Harry", "Ron"]


# print(students[0])
# print(students[1])
# print(students[2])


# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i+1, students[i])



# students = ["Hermione", "Harry", "Ron"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor"]

#using dictionaries
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# #when we use for loop with dictionaries, we are iterating over the keys of the dictionary
# for student in students:
#     print(student, students[student], sep=": ")

#we want to use a list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

# Print the table once using tabulate
print(tabulate(students, headers="keys"))
print()
# Print each student's information
for student in students:
    print(f"Name: {student['name']}, House: {student['house']}, Patronus: {student['patronus']}")

