#anonymous function - a funtion without a name. used as a tiny function
#ways to use anon functions:
# set a variable to an anon function without having to define it or its name. A quick way to define a funtion and use is

#traditional function to double a number:
# def double_number(number):
#     doubled = number * 2
#     return doubled

# double = double_number(5)
# print(double)

#lambda way - use an expression (=) to define a function using an anon function inside. Named after lambda calculus

double = lambda number: number * 2
print(double(5))

#multiple parameters
multiply = lambda first,second: first * second
print(multiply(5,7))