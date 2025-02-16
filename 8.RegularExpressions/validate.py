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
# email = input("Whats your email? ")
# username, domain = email.split("@")

# if username and domain.endswith("edu"):
#     print("Valid")

# else:
#     print("Invalid")

    

#8.4
#re.search(pattern, string, flags=0)
"""
This script prompts the user to input an email address and checks its validity using a regular expression.

Steps:
1. The `re` module is imported to use regular expressions for pattern matching.
2. The script takes user input using the `input()` function and stores it in the variable `email` after removing any leading or trailing whitespace using the `.strip()` method.
3. A regular expression (`.*@.*`) is used to check if the email contains the `@` symbol:
   - `.*` matches zero or more of any character (except newlines).
   - `@` matches the literal `@` symbol.
   - Together, `.*@.*` ensures that the input contains at least one `@` with characters on either side (though it can also match empty strings before or after the `@`).
4. The `re.search()` function searches for the pattern in the `email` string:
   - If the pattern is found, it means the input contains an `@` symbol, and the script prints "Valid".
   - If the pattern is not found, the script prints "Invalid".
5. The script does not validate the email address format beyond checking for the presence of the `@` symbol. It considers inputs like "@" or "@example" as valid, which may not meet standard email validation criteria.

This is a simple validation and should be improved to fully validate email addresses.
"""

# import re
# email = input("Whats your email? ").strip()

# #check if @ is in the email
# if re.search(".*@.*", email):
#     print("Valid")
# else:
#     print("Invalid")

"""
. : any character except a newline
*: 0 or more repitions
+: 1 or more repitions
?: 0 or 1 repitition
{m} : m repititions
{m,n}: m-n reptitions
"""

#8.5
"""
This script validates an email address entered by the user, using a regular expression to check for the presence 
of characters before and after the "@" symbol.

Steps:
1. The `re` module is imported to facilitate pattern matching using regular expressions.
2. The script prompts the user to input an email address using the `input()` function. 
   The input is stripped of leading and trailing whitespace using the `.strip()` method and stored in the variable `email`.
3. A regular expression (`.+@.+`) is used to validate the email:
   - `.+` matches one or more of any character (except newlines).
   - `@` matches the literal `@` symbol.
   - Together, `.+@.+` ensures that the input contains:
       a. At least one character before the `@`.
       b. At least one character after the `@`.
4. The `re.search()` function is used to search for the pattern in the `email` string:
   - If the pattern is found, the input meets the minimal criteria for an email, and the script prints "Valid".
   - If the pattern is not found, the input does not meet the criteria, and the script prints "Invalid".
5. Limitations:
   - This script does not enforce complete email validation according to the standards defined in RFC 5322.
   - Inputs such as "a@b" or "user@domain" will be considered valid, even though they might not be realistic email addresses.
   - Further checks could be added to verify domain formats, valid characters, and top-level domains.
"""

# import re
# email = input("Whats your email? ").strip()

# if re.search(".+@.+", email):
#     print("Valid")
# else:
#     print("Invalid")



#8.6
"""
This script validates an email address entered by the user using a simple regular expression 
to check for the presence of at least one character before and after the "@" symbol.

Steps:
1. The `re` module is imported to enable regular expression pattern matching.
2. The user is prompted to input an email address using the `input()` function.
   - The `.strip()` method removes any leading or trailing whitespace from the input.
   - The resulting string is stored in the `email` variable.
3. A regular expression pattern (`..*@..*`) is used to validate the email structure:
   - `..*` before the `@`:
       - `.`: Requires at least one character before the `@`.
       - `.*`: Allows zero or more characters after the first character.
   - `@`: Matches the literal "@" symbol in the email.
   - `..*` after the `@`:
       - `.`: Requires at least one character after the `@`.
       - `.*`: Allows zero or more characters after the first character.
4. The `re.search()` function checks if the `email` matches the regular expression:
   - If the email matches the pattern:
       - The script prints "Valid".
   - If the email does not match the pattern:
       - The script prints "Invalid".
5. Examples:
   - **Valid:**
       - `a@b.com`: Matches because there is at least one character before and after the `@`.
       - `e@harvard.edu`: Matches because it satisfies the pattern.
       - `1@2`: Matches because there is one character before and after the `@`.
   - **Invalid:**
       - `@domain.com`: Fails because there is no character before the `@`.
       - `user@`: Fails because there is no character after the `@`.
6. Limitations:
   - This pattern enforces only a minimal structure for an email.
   - It does not validate domains, special characters, or full compliance with email formatting standards.
"""

# import re
# email = input("Whats your email?").strip()

# if re.search("..*@..*", email):
#     print("Valid")

# else:
#     print("Invalid")

#8.7
"""
This script validates if an input email address is in a valid format with the domain `.edu`.

Steps:
1. The user is prompted to input an email address.
2. The input is stripped of any leading or trailing whitespace.
3. The email is then checked using a regular expression to see if it matches the pattern for a valid email ending with `.edu`.

Regular Expression Breakdown:
- `.+`: Matches at least one character before the `@` symbol (the local part of the email).
- `@`: Matches the literal `@` symbol separating the local part and domain.
- `.+`: Matches at least one character after the `@` symbol (the domain part).
- `\.edu`: Matches the literal string `.edu` at the end of the domain.

If the input matches the pattern, the script prints "Valid", otherwise it prints "Invalid".

Example of a valid email:
    - `user@university.edu`

Example of an invalid email:
    - `user@domain.com`

The script ensures that the email address must end with `.edu` to be considered valid.
"""
# []: match any character inside the square brackets
# [^]: match any character not inside the square brackets
# [^@]: match any character that is not @
# import re
# email = input("Whats your email? ").strip()

# if re.search(r"^[^@]+@[^@]+\.edu$",email):
#     print("Valid")

# else:
#     print("Invalid")




# import re
# email = input("Whats your email? ").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
#     print("Valid")

# else:
#     print("Invalid")
    

#we can get ride of the entire [a-zA-Z0-9_] by using \w
# \w: match any alphanumeric character and underscore

# import re
# email = input("Whats your email? ").strip()

# if re.search(r"^\w+@\w+\.edu$",email):
#       print("Valid")
# else:
#       print("Invalid")


#  \d: match any digit
#  \D: match any non-digit
#  \s: match any white space
#  \S: match any non white space
#  \b: match word boundaries
#  \B: match non-word boundaries
#  \A: match beginning of string
#  \Z: match end of string
#  \w: match any alphanumeric character and underscore


# if I want to accept .edu, .com, .net, .org
# import re

# email = input("Enter your email: ").strip()

# if re.search(r"^\w+@\w+\.(edu|com|net|org)$", email):
#     print("Valid")
# else:
#       print("Invalid")


#if we want the domain to be case insensitive
# re.IGNORECASE or re.I: ignore case
# import re

# email = input("Enter your email: ").strip()

# if re.search(r"^\w+@\w+\.(edu|com|net|org)$", email, re.IGNORECASE):
#       print("Valid")

# else:
#       print("Invalid")


#re.MULTILINE or re.M: treat beginning and end characters (^ and $) as working for each line
#re.VERBOSE or re.X: allows for comments and whitespace in the pattern
#re.DOTALL or re.S: make the . match any character, including newlines



# import re

# email = input("Enter your email: ").strip()

# if re.search(r"^\w+@\w+\.\w+\.(edu|com|net|org)$", email, re.IGNORECASE):
#       print("Valid")

# else:
      # print("Invalid")


#the above code will only work for emails that have two domains, 
#hence an email malan@harvard.edu will be invalid
#to fix this we can use the following code
import re

email = input("Enter your email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|net|org)$", email, re.IGNORECASE):
      print("Valid")

else:
      print("Invalid")