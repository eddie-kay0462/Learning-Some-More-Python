class Student:
    #dunder method, constructor. It is called when an object is created
    def __init__(self, name, house):
        self.name = name
        self.house = house
    

    ##dunder method, called when we print the object
    def __str__(self):
        return f"{self.name} from {self.house}"

    ##getter for name
    @property
    def name(self):
        return self._name

    ##setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is required!!")
        self._name = name

    ##getter method
    @property #this is a decorator. It is used to define a property in a class. It allows us to access the method as an attribute
    def house(self):
        return self._house

    ##setter method
    @house.setter #the setter method is used to set the value of the attribute of the class 
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("House is not valid!!")
        self._house = house
    
def main():
    student = get_student()
    
    print(student)


def get_student():
    name = input("Enter student's name: ")
    house = input("Enter student's house: ")
    return Student(name, house)
   


if __name__ == "__main__":
    main()