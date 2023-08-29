# for loop or count controlled loop iterates (learn this word... means to go over or through a series of something) a certain number of times. 
# that count can be based on a number range or how many items are in a data set such as a list (we will do this later, and is the most common use for a for-loop)

#for loop example
number = 10
countdown = 0

# traditional programming language works a bit different than python for for loops. Below is what one looks like throuhg another language:
# for(i=0, i < number; i++)

#python, instead, uses a range funtion to do the same thing. The range function uses 3 arguments to accomplish this
#for iteratorvariable in range - (startingvalue, endingvalue, increment)
for i in range(0, number, 1):
    print(i)

print(" ")

#countdown or decrement
for i in range(10, countdown, -1):
    print(i)