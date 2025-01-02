import cowsay
import sys

# if len(sys.argv) == 2:
#     cowsay.cow(sys.argv[1])
# else:
#     print("Usage: python say.py <message>")


#we can use the trex function to say something
if len(sys.argv) == 2:
    cowsay.trex(sys.argv[1])
else:
    print("Usage: python say.py <message>")
