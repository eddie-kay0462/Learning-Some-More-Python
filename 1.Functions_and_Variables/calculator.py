# x = int(input("Whats x: "))
# y = int(input("Whats y: "))

x = float(input("Whats x: "))
y = float(input("Whats y: "))

# z = round(x + y)



# print(f"{z:,}") #this is a formatted string, it is a string that has a format specifier. The format specifier is a colon followed by a comma. The comma is a comma separator.


#z= round(x / y, 2) #this is a division operation. It will return a float. The round function is used to round the result to 2 decimal places.

#we can also use the .2f to format the result to 2 decimal places.
z = x / y

print(f"{z:.2f}")