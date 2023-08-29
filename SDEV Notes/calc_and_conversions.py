#calculations in python consist of your typical math calculations (- + / *)
#modulo or modulus - take two numbers, divide them, and the remainder is the result of the modulus calculation

a = 7
b = 10

answer = a + b
print(answer)

c = 7
d = 4
product = c * d
print(product)

#modulo (divides two numbers and result in remainder. uses % sybmol to perform modulo operation)
e = 5
f = 2
answer2 = e % f
print(answer2)

#exponents use **
answer3 = 10 ** 3
print(answer3)

#utilizing inputs to calculate
#input from a user, it comes in the form a string. The problem is that strings combine (concatanate), but that is about the only operation you can perform on a string

#wrong wat to calculat using inputs
i = input("Give me a first number: ")
f = input("Give me a second number: ")
total = i + f
print(total)

#convert or parse our inputs into calculable variables/types. You can do this through a function. There are 2 types.
#int() - converts veriables to a integer
#float() - converts variables to a float

g = float(input("Give me the first number to be calculated: "))
h = float(input("Give me the second number to be calculated: "))
total2 = g + h
print(total2)
