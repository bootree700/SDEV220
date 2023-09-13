# Author: Dylan Moreland
# Program: M03_Lab.py
# Purpose: Accept information about the car and display it in an easy to read format
# Variables: type => stores the vehicles type, part of the 'Vehicle' class. Also used in the subclass, Automobile.
#            year, make, model, doors, roof => stores the information their names indicate, part of the subclass Automobile.


# Initialize the Vehicle Class
class Vehicle:
    type = "type"

# Initialize the Automobile Class, a subclass of Vehicle
class Automobile(Vehicle):
    year = 0
    make = "make"
    model = "model"
    doors = 0
    roof = "roof"

# Initialize the instance vehicle_1
vehicle_1 = Automobile()
# Accept user inputs and set the data in the class as the inputs
vehicle_1.type = input(str("What is the vehicle type?: "))
vehicle_1.year = input("What year is the %s?: " % (vehicle_1.type))
vehicle_1.make = input(str("What make is the %s?: " % (vehicle_1.type)))
vehicle_1.model = input(str("What model is the %s?: " % (vehicle_1.type)))
vehicle_1.doors = input("How many doors does the %s have?: " % (vehicle_1.type))
vehicle_1.roof = input(str("What kind of roof does the %s have?: " % (vehicle_1.type)))

# Reprint the data in a neat format
print(" ")
print("Vehicle type:", vehicle_1.type)
print("Year:", vehicle_1.year)
print("Make:", vehicle_1.make)
print("Model:", vehicle_1.model)
print("Number of doors:", vehicle_1.doors)
print("Type of roof:", vehicle_1.roof)