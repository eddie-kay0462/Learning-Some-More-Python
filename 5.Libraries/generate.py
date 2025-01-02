# from random import choice

# #the choice function is used to choose a random element from a list
# coin = choice(["head", "tail"])
# print(coin)

#using randint to generate a random integer between two numbers (inclusive)
from random import randint
number = randint(1, 10)
print(number)


#using the shuffle function to shuffle a list
from random import shuffle
cards = ["jack", "queen", "king", "whatever"]
shuffle(cards)
print(cards)


