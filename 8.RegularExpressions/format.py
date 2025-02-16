import re

# name = input("What is your name? ").strip()

# if "," in name:
#     last, first = name.split(", ?")
#     name = first + " " + last
    
    

# print("Hello, {}!".format(name))

# 2
# name = input("What is your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)

# if matches:
#     name = matches.group(2) + " " + matches.group(1)

# print("Hello, {}!".format(name))

#in the above code, we are using regular expression to match the name entered by the user.
#we are using the search method to search for the pattern in the string.
#the pattern is ^(.+), (.+)$
# ^ - start of the string
# (.+) - match one or more characters
# , - match a comma
# (.+) - match one or more characters
# $ - end of the string
# if the pattern is found, the search method returns a match object.
# we can use the group method to access the matched groups.
# group(0) returns the entire matched string.
# group(1) returns the first matched group.
# group(2) returns the second matched group.


# name = input("What is your name? ").strip()

# #addition of ? after the space " " makes the space optional
# #this is because the space is optional in the name entered by the user
# matches = re.search(r"^(.+), ?(.+)$", name)

# if matches:
#     name = matches.group(2) + " " + matches.group(1)

# print("Hello, {}!".format(name))



#3

name = input("What is your name? ").strip()

#we can use the * quantifier to match zero or more spaces

if (matches := re.search(r"^(.+), *(.+)$", name)):
    name = matches.group(2) + " " + matches.group(1)
print("Hello, {}!".format(name))


#in the above code, we are using the walrus operator to assign the result of the search method to the matches variable.