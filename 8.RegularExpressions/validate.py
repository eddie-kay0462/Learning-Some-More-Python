# email = input("Whats your email? ")
# if "@" in email and "."  in email:
#     print("Valid")
# else:
#     print("Invalid")

#8.2
# email = input("Whats your email? ")
# username, domain = email.split("@")

# if username and "." in domain:
#     print("Valid")

# else:
#     print("Invalid")


#8.3
email = input("Whats your email? ")
username, domain = email.split("@")

if username and domain.endswith("edu"):
    print("Valid")

else:
    print("Invalid")

    