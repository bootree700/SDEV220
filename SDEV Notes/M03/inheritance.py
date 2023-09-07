class Parent():

    def print_last_name(self):
        print("Roberts")

class Child(Parent): #adding a class to the parenthesis causes the Child class to inherit the functions of the Parent Class

    def print_first_name(self):
        print("Bucky")

    def print_last_name(self): #this can overwrite the function from the parent class
        print('Snitzelberg')


bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

