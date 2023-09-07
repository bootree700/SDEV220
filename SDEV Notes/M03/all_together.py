#class that represents a person. Maybe we are making an employee program to keep track of sales and salary

class Person():
    def __init__(self, name, age, sales, salary):
        self.name = name
        self.age = age
        self.sales = sales
        self.salary = salary

    def mySales(self):
        print("My sales are", self.sales)
    def mySalary(self):
        print("My salary is", self.salary)
    def net_value_company(self):
        print("The net value of",self.name, "is", self.sales - self.salary)

sum = 0

#create instances
person1 = Person("Zach",38,5000,30000)

person1.mySales()
person1.mySalary()
person1.net_value_company()

person2 = Person("Tim",40,100000,35000)
person2.mySales()
person2.mySalary()
person2.net_value_company()

list_of_employees = [person1,person2]

for person in list_of_employees:
    person.mySalary()
    sum = sum + person.salary

print("Our total employee cost is", sum)