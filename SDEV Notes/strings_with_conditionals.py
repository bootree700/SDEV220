#comparing string must be exact to say they are equal

name = "Zach"
name2 = "zach"

if (name == name2):
    print("names the same")
else:
    print("names are not the same. capital letters matter!")

choice = input("Do you wish to continue? enter y to continue: ")

if (choice == "y" or choice == "Y"):
    print("You have chosen to continue")
else:
    print("Goodbye!")