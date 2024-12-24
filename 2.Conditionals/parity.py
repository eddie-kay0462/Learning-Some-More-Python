# Version 1: Basic Implementation
# Simple if/else in main program
# Straightforward but not modular
x = int(input("Whats x: "))
if x % 2 == 0:
   print("x is even")
else:
   print("x is odd")

# Version 2: Function with explicit return
# Introduces modularity via parity() function
# More reusable but verbose returns
def main():
   x = int(input("Whats x: "))
   if parity(x):
       print("even")
   else:
       print("odd")

def parity(x):
   if x % 2 == 0:
       return True
   else:
       return False

# Version 3: Function with implicit return
# Final evolution - most concise
# Returns boolean expression directly
def parity(x):
   return x % 2 == 0

if __name__ == "__main__":
   main()