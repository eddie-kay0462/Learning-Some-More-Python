import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod #class methods are used to define methods that are not connected to the instance of the class but to the class itself
    def sort(cls,name):
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")




Hat.sort("Eddie")