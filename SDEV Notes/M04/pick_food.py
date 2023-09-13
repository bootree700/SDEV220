#import a package (that you would get from pip or other online sources) or a module (usually created by you or the python library). 
#Random module - Have various classes/functions to randomly generate or pick something

#import statement - you can import all functions/methods or just ones you want to use.

from random import choice

#randomly choose a restaurant from a list
places = ["McDonalds", "KFC", "Arbys", "Pizza Hut"]

def pick():
    #return a random food restaurant from a list
    return choice(places)

#my_choice = choice(places)
#print(my_choice)

