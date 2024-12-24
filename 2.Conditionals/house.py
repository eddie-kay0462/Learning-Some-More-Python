# Version 1: Multiple OR conditions
# Traditional if/elif/else with multiple OR operators
# More familiar to beginners, works in all Python versions
name = input("Enter your name: ")
if name == "Harry" or name == "Hermione" or name == "Ron":
   print("Gryffindor")
elif name == "Draco":
   print("Slytherin")
else:
   print("Who?")

# Version 2: Match-case (Python 3.10+) 
# Uses pattern matching with OR patterns (|)
# More concise and cleaner for multiple conditions
match name:
   case "Harry" | "Hermione" | "Ron":
       print("Gryffindor")
   case "Draco":
       print("Slytherin")
   case _:  # Default case
       print("Who?")