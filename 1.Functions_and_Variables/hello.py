#ask user for their name
name = input("Whats your name: ").strip().title() #we can chain methods together. Over here we are removing the white space from the beginning and end of the string and then capitalizing the first letter of the string.
# #say hello to the user as a welcome message
# print("Hello,",name)



#use print two times
#the sep is the separator between the two print statements, it is a space by default. 
# print("Hello,", name, sep=" ")
# print(name)

#the end is the end of the print statement, it is a newline by default.
#print("Hello,", name, end="\n")  #this is the end of the print statement, we can change it to anything we want. e.g. end="\t"
#print(name) #this is the end of the print statement


#we can use f strings to format the output
# print(f"Hello, {name}, welcome to the python course")


#remove the white space from the beginning and end of the string
# name = name.strip()
# print(f"Hello, {name}, welcome to the python course")


#we can capitalize the first letter of the string
# name = name.strip().capitalize()
# print(f"Hello, {name}, welcome to the python course")


#we can capitalize the first letter of each word in the string
# name = name.strip().title()
# print(f"Hello, {name}, welcome to the python course")

#split user input into first name and last name
first_name, last_name = name.split(" ")
print(f"Hello, {first_name}, welcome to the python course!")

