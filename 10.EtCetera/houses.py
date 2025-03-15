students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
    {"name": "Ron", "house": "Gryffindor"},
]

houses = set()
          
for student in students:
    houses.add(student["house"])


for house in sorted(houses):
    print(house)