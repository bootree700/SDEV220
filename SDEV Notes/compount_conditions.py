# logic operators - and, or, not. Create a series of complex statements that determine if a block of code will run
# in many cases, logic operatiors help limit the need or use of nested if statements
# and - where both conditions must be true for the block of code to run
# or - where only one condition must be true for the block of code to run
# not - takes the opposite value of the boolean (T/F) that is the result of a comparison and flips or changes it

#create a program that determines if you can get a loan based on salary and number of years worked. 
#If you have worked 2 or more years and have a salary >=30000, you qualify for a loan.
#We will also tell the user the reason why they do not qualify.

salary = float(input("Enter your yearly salary:" ))
years_worked = int(input("Enter the amount of years you have worked: "))

if (salary >= 30000 and years_worked >=2):
    print("You qualify for a loan")

#make enough money, but not enouhg years worked

elif(salary >= 30000 and years_worked <2):
    print("You have not worked long enough to qualify for a loan")

#worked long enough, but our salary is too low
elif(salary < 30000 and years_worked >= 2):
    print("Your current salary is too low to qualify for a loan")

else:
    print("You do not meet either requirement for a loan")