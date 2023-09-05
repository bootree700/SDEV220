#returm functions are like void/non-return functions, except they return a value into a variable. You can also use default parameters to set a default value.

#create a return function with a default paramete
def add_numbers(number1, number2, number3=10):
    sum = number1 + number2 + number3
    return sum

#take in lists as parameters
def print_items(items):
    for item in items:
        print(item)

my_sum = add_numbers(10, 15)
print(my_sum)

#use non-default parameter
my_sum2 = add_numbers(10,15,8)
print(my_sum2)

food = ["apple", "orange", "pizza"]
print_items(food)