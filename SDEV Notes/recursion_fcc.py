#funtions as first-class citizens. A funtion taking in another function as an argument. Chanining functions together

x = "66"
print(int(x))

def add_numbers(number1, number2, number3=10):
    sum = number1 + number2 + number3
    return sum

print(add_numbers(5,4))

#recursion - funtion that calls iteslf over and over until a condition is met. the funtion version of a loop (sort of)
#this function will run until the initial number reaches 0, then it will end the funtion
def countdown(number):
    if number == 0:
        return
    else:
        print(number)
        countdown(number - 1)

countdown(5)