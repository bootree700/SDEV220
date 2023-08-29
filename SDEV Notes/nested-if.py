# nested if statement (an if statement inside of another if statement)
# multi-alternative - there can be 2 or more decisions or 'paths' for the applications to go down.
# this program below will tell you what type of animal you are based on if you are a large creature, a furry creature, or both.
# we will use boolean(True/False) as flags to determine this

furry = False
large = False

if furry:
    if large:
        print("You are a Yeti")
    else: 
        print("You are a cat")
else:
    if large:
        print("You are a whale")
    else:
        print("You are a human")
    