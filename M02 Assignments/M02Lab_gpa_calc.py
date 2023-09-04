# Programmer Name: Dylan Moreland
# Program Name: M02Lab_gpa_calc.py
# Purpose: Accept student name and GPA and determine eligibility for deans list
# Variables: last_name - stores and displays the student's last name as input by the user, gpa - stores and displays the student's gpa as input by the user

last_name = str(input("Please enter the student's last name or 'ZZZ' to end: ")) #Asks for last name input or ending statement

#Begins a while loop, ending when last_name is set to "ZZZ"
while last_name != "ZZZ": 
    first_name = str(input("Please enter the student's first name: ")) #asks for first name input

    gpa = float(input("Please enter %s %s's GPA: " % (first_name, last_name))) #Asks for gpa input, %s and variables after the text allows the name to be displayed in the input request

    #Begins an if statement, evaluating eligibility for the Dean's List and Honor roll based upon input gpa
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll")
    else:
        print(first_name, last_name, "has not made the Dean's List or the Honor Roll. :(")
    
    last_name = str(input("Please enter the student's last name or 'ZZZ' to end: ")) #Reprints initial statement, breaking loop and ending the program if "ZZZ is ented"

print("Thank you for using the program. Goodbye!") #Program End statement