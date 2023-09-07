#classes can represent real objects with data that can be changed or modified depending on what we need to do with the class instance

#We can also use instance variables
#instance variables can be set or changed upon the creation of an instance

#create a class called Monkey. Monkey will have a couple attributes - name and animal. Monkey will always have animal = monkey. (class variable)
#however, we can chance the name of each moneky upon instantiation (creation)

class Monkey:
    #class variable that will not change no matter how many instances of the monkey class we make. It can be changed after we create an instance of the monkey class.
    animal = "Monkey"
    #now we know everytime we create a new monkey, animal = "Monkey". However we will make animals have differnt names below

    #constructor or init - initialize the instance variable with some data that the user or other parts of the program provide it.
    #method - funtion inside of a class or a function that belongs to an object
    #self - that individual's instance's value or variables
    def __init__(self,name):
        self.name = name

#create monkeys
monkey1 = Monkey("Tom")
print(monkey1.animal)
print(monkey1.name)

#instance 2
monkey2 = Monkey("Jim")
print(monkey2.animal)
print(monkey2.name)