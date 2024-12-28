##Dictionaries Practice

#first dictionary
name_school = {
    "Edward": "Harvard",
    "John": "Yale",
    "Sam": "Princeton"

}

#second dictionary
name_school2 = {
    "William": "Ashesi",
    "Eli": "MIT",
    "Kofi": "Yale"
}

#merging dictionaries using update
# name_school.update(name_school2)
# print(name_school)

#merging dictionaries using the pipe operator
# merged_dict = name_school | name_school2
# print(merged_dict)

#merging dictionaries using the double star operator
# merged_dict = {**name_school, **name_school2}
# print(merged_dict)

#practice with sep 
print("Hello", "World", sep="...") #this will print Hello...World. this is because the sep is the separator between the two strings
