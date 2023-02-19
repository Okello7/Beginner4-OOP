#OOP
#Class Blueprint  of an object
#Objects instance of a class
#Methods implements behavioof an object
#Inheritance Norma such as family line
#polymorphism Having smth in diffferent forms
#Abstraction inding the internal of an application
#encapsulation

#className_of_class:
#   classs variables
#   methods or functions

class Dog:
    #variables
    #name = "Bosco"
    #color = "black"
    #breed = "GS"
    def __init__(self, name, color,breed):
        self.name= name
        self.color = color
        self.breed = breed


    #functions/method behaviour
    #an eat, move, bark
    def eat(self):
        return("Dog needs to eat")
    
    def bark(self):
        return("Dog is barkiing")
    
    
#Instantiation
dog1 = Dog("Bosco", "Black", "GS")
dog2 = Dog("Suu", "Grey", "BD")

#Accessing  methods and variables in class
print(dog1.breed)
print(dog2.eat())
print(dog1.__dict__)
print("Dog 2 details ",dog1.__dict__)

    

