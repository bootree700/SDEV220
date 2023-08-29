#create a program that averages numbers together
#average = sum of numbers / total amount of numbers

total_sum = 0
average = 0

how_many_numbers = int(input("How many numbers do you want to be averaged?: "))

for i in range (0, how_many_numbers, 1):
    value = float(input("Please enter a value you wish to be averaged: "))
    total_sum = total_sum + value

average = total_sum / how_many_numbers

print("Your total is:", total_sum)
print("Your average is:", average)