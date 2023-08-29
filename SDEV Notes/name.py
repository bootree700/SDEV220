#variables store data
#weakly typed language - variables have types, but you do not have to declare the type before initializing the variable

#types:
#int - whole numbers
#floats - decimal numbers
#strings - text
#boolean - True/False

x = 6 #int
y = 7.6 #float
name = "Dylan" #string
bool_example = True #bool

#functions - perform actions, take inputs process the input and produce and output
#input function - takes an input and returns it into a variable. The text inside of the () is called an argument. The input arguments ared used to display a prompt to the user
#functions are denoted by the () in their name (this is the difference between knowing something is a variable vs a function)
name2 = input("What is your name? ")

#print function displays something one screen in the form of a string. What is displayed is whatever is put into the print function's argument
print("Your name is", name2)

#incrementation - taking the current value of a variable and adding somethng to it

z = 8
print(z)
z = z + 2
print(z)