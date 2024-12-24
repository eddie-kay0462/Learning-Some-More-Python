# Version 1: Most Explicit
# Uses explicit upper and lower bounds for each grade range
# Advantages: Very clear logic, good for teaching/learning
# Disadvantages: More verbose, redundant comparisons
score = int(input("Enter your score: "))
if score >= 90 and score <= 100:
   print("score: A")
elif score >= 80 and score < 90:
   print("score: B")
elif score >= 70 and score < 80:
   print("score: C")
elif score >= 60 and score < 70:
   print("score: D")
else:
   print("score: F")

# Version 2: Chain Comparison
# Uses Python's ability to chain comparisons
# Advantages: More mathematically intuitive, cleaner syntax
# Built upon Version 1 by removing redundant comparisons
if 90 <= score <= 100:
   print("score: A")
elif 80 <= score < 90:
   print("score: B")
elif 70 <= score < 80:
   print("score: C")
elif 60 <= score < 70:
   print("score: D")
else:
   print("score: F")

# Version 3: Simplified Logic  
# Leverages sequential checking to eliminate redundant bounds
# Final evolution - most efficient while maintaining readability
if score >= 90:
   print("score: A")
elif score >= 80:
   print("score: B")
elif score >= 70:
   print("score: C")
elif score >= 60:
   print("score: D")
else:
   print("score: F")