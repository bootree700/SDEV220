# Programmer Name: Dylan Moreland
# Program Name: M02Lab_gpa_calc.py
# Purpose: Accept student name and GPA and determine eligibility for deans list

student_name = str(input("Please enter the student's first name or 'ZZZ' to end: "))

while student_name != "ZZZ":
    gpa = float(input("Please enter {}'s GPA: ".format(student_name)))

    if gpa >= 3.5:
        print(student_name, "has made the Dean's List.")
    elif gpa >= 3.25:
        print(student_name, "has made the Honor Roll")
    else:
        print(student_name, "has not made the Dean's List or the Honor Roll. :(")
    
    student_name = str(input("Please enter the student's first name or 'ZZZ' to end: "))

print("Thank you for using the program. Goodbye!")