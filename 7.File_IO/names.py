#7.1
# names = []
# for _ in range(3):
#     names.append(input("Whats your name? "))


# for name in sorted(names):
#     print(f"Hello {name}")

#7.2
# name = input("What's your name? ")

# file = open("names.txt", 'w') 
# file.write(name)
# file.close()


#7.3
# file = open("names.txt", 'a')
# file.write(f"{name}\n")
# file.close()

#7.4
# with open("names.txt", 'a') as file:
#     file.write(f"{name}\n")

#7.5
#we are writing code to read an existing file
# with open('names.txt', 'r') as file:
#     lines = file.readlines()

# for line in lines:
#     # print(f"Hello {line}", end='')
#     print(f"Hello {line.rstrip()}")

#7.6
#a numch cleaner way to do it
# with open('names.txt', 'r') as file:
#     for line in file.readlines():
#         print(f"Hello, {line.rstrip()}")

#7.7
#even more cleaner
# with open("names.txt", 'r') as file:
#     for line in sorted(file):
#         print(f"Hello, {line.rstrip()}")

#7.8
names = []

#if you are opening a file in read mode you don't have to specify the r mode, thats the default!!
with open("names.txt") as file:
    for line in file:
        names.append(line.strip())


#the default for reverse is false, and we can change it to True
for name in sorted(names, reverse=True):
    print(f"Hello {name}")