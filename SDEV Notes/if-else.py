#if-else statements are known as dual alternative. If a statement is true, the path will flow to the if statement. 
#If false (or all other alternatives), it will run the else statement's block of code.

a = 7
b = 9
if (a == b):
    print("A and B are equal")
else:
    print("A and b are not equal")

# can you vote application. The code below will test to see if someone is old enough to vote.

age = int(input("Please enter your age: "))
if (age >= 18):
    print("You are old enough to vote!")
else: 
    print("You are not old enough to vote...")