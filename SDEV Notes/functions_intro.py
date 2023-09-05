#functions take data in, transform it, and output it
#funtions consider actions (verb)
#funtions are a block of code that can be repeated when it's name is called.
#It can also have data passed to it, and can return data as a result.

# to create our own fucntion, we first have to define it
def my_funtion():
    x = 10
    y = 15
    print (x + y)

#passing data to a funtuion - creata a parameter
#funtion variable is a placeholder
def display_number(my_number):
    print(my_number)

#a function can take in multiple parameters. It an also manipulate the incoming data
def add_numbers(number1, number2):
    sum = number1 + number2
    print(sum)


my_funtion()
my_funtion()

display_number(4)
numb = 43
display_number(numb)

add_numbers(5,4)
first_num = 30
second_num = 80
add_numbers(first_num, second_num)