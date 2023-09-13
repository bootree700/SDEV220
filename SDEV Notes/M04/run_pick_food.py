#import pick_food into this program. We have multiple ways of importing 

#comment out the ones you don't want to use

#first way of importing and running will be aliasing
# import pick_food
# place = pick_food.pick()
# print("Lets go to", place)

#second way is giving it an alias
# import pick_food as mypick
#similar to saying mypick = pick_food.py
# place = mypick.pick()
# print("Lets go to", place)

#final way is importing specific functions from a module that you want to use

from pick_food import pick
place = pick()
print("Lets go to", place)
