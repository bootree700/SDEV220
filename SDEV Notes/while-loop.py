#loops are also control structures. They repeat code until a condition is met. They use the same logic and relational operatiors as if-else statements.
# the main goal of a loop is to repeat code until you don't want the code repeated.

#two types of loops - while/for

#while loop - a loop that repeats code based on a condition - for the most part we do this through a sentinel value or a flag

#program that will record and calculate comission of an employee until the user wants the program to stop

#flag or sentinel value
keep_going = "y"
print("Enter the following to calculate your sales and comissions. When you are done, at the end of the program, press the letter n and enter to stop it.")

while(keep_going == "y"):
    sales = float(input("Enter your sales amount for the week: "))
    com_rate = float(input("Enter your commission percentage as a decimal: "))
    total_earned = sales * com_rate
    print("Your total commission is", total_earned)
    keep_going = input("Do you wish to continue? Press y and enter to continue or n and enter to exit: ")

print("Thanks for using our program!")