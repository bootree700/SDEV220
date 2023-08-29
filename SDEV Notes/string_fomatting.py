#string formatting uses an f and braces inside of a print funtion to create placeholders and format strings

number = 6
amount = 5.979785

#traditional way
print("I bought", number, "burritos, and it cost me $", amount)

#string formatting
print(f'I bought {number} burritos, and it cost me ${amount}')