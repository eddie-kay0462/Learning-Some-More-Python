# url = input("Enter the URL: ").strip()

# username = url.replace("https://twitter.com/", "")

# print(f"Username: {username}")


#2
# url = input("Enter the URL: ").strip()

# username = url.removeprefix("https://twitter.com/") # removeprefix is a new method in Python 3.9 that removes a prefix from a string

# print(f"Username: {username}")



#
# import re


# url = input("Enter the URL: ").strip()

# #re.sub(pattern, repl, string, count=0, flags=0): Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.

# username = re.sub(r"(https?://)?(www\.)?twitter\.com/", "", url)

# print(f"Username: {username}")




import re


url = input("Enter the URL: ").strip()



# if match := re.search(r"https?://(www\.)?twitter\.com/(.+)", url, re.IGNORECASE): #re.IGNORECASE ignores the case of the string
#     print(f"Username: {match.group(2)}") #group(2) returns the second group in the match object


#we can use the non capturing group (?:) to avoid creating a group for the entire URL

if match := re.search(r"https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE): #re.IGNORECASE ignores the case of the string
    print(f"Username: {match.group(1)}") #group(1) returns the first group in the match object