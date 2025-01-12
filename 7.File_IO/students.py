#s7.1
# with open("students.csv") as file:
#     for line in file:
#         row =  line.rstrip().split(',')
#         #instead of the line above, we can inpack the row simultaneously into two variables
#          # print(f"{row[0]} is in {row[1]}")
#         name, house, = line.rstrip().split(',')
#         print(f"{name} is in {house}!")


#s7.2
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# for student in students:
#     print(f"{student["name"]} is in {student["house"]}")



#s7.3
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name":name, "house":house}
#         students.append(student)
# #returns the name for a particular student
# def get_name(student):
#     return student["name"]

# #returns the house for a particular student
# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student["name"]} is in {student["house"]}!")



#s7.4
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name":name, "house":house}
#         students.append(student)

# #instead of having functions such as get_name and get_house, I could use an anonymous function in the
# #sorted function
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student["name"]} is in {student["house"]}!")

#s7.5
# students = []
# with open("students1.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name":name, "home":home}
#         students.append(student)

# #instead of having functions such as get_name and get_house, I could use an anonymous function in the
# #sorted function
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student["name"]} is in {student["home"]}!")



import csv
# #s7.6
# students = []
# with open("students1.csv") as file:
#     reader = csv.reader(file)
#     # for row in reader:
#     #     students.append({"name": row[0], "home": row[1]})
#     #even more tighter
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# #instead of having functions such as get_name and get_house, I could use an anonymous function in the
# #sorted function
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student["name"]} is from {student["home"]}!")

#we can bake the information about the columns in the row of the file (csv)
#s7.6
# students = []
# with open("students1.csv") as file:
#     #due the placing of the actual column names in the csv file we will now use a 
#     #Dict reader instead of just a normal reader
#     #the Dict reader returns a dictionary
#     reader = csv.DictReader(file)
#     # for row in reader:
#     #     students.append({"name": row[0], "home": row[1]})
#     #even more tighter
#     for row in reader:
            #students.append(row) #this also works because the row is a dictionary
#         students.append({"name": row["name"], "home": row["home"]})

# #instead of having functions such as get_name and get_house, I could use an anonymous function in the
# #sorted function
# for student in sorted(students, key=lambda student: student["name"], reverse=True):
#     print(f"{student["name"]} is from {student["home"]}!")



#writing to CSV files
#s7.7
# name = input("What's your name? ")
# home = input("What's your home? ")
# with open("students2.csv", 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow()

#s7.8
#we will now use a Dict write so as not to worry about the order of the columns
name = input("Whats your name? ")
home = input("What's your home? ")
with open("students2.csv", 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


