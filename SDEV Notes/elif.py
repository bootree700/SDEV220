# elif (else-if) are often used to categorize or eliminate data
# Grading program. Take a number and turn it into a letter grade. We will only focus on A, B, and C. The scale will be A=90-100, B = 80-89, C = 70-79. 
# Everything below a 70 will be a fail

number_grade = int(input("Enter your number grade as a whole number: "))

if (number_grade >= 90):
    print("Your letter grade is an A")
elif(number_grade >=80):
    print("Your letter grade is a B")
elif(number_grade >= 70):
    print("Your letter grade is a C")
else:
    print("You failed")