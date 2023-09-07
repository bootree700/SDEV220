#to privatize variables (make them non-accessible to any outside of the class) use __
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    #getters and setters - getters grab data, setters modify

    #getters
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    
    #setters
    def set_name(self,name):
        self.__name = name
    def set_name(self,animal_type):
        self.__animal_type = animal_type
    def set_name(self,age):
        self.__age = age

mypet = Pet("Braxton", "dog", 10)
print(mypet.get_name())
print(mypet.get_age())
mypet.set_name("Barkley")
print(mypet.get_name())
