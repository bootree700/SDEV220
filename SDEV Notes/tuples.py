#data structures - ways to structure data in a meaningful way. Store multiple values in some type of order or category
#tuples are immutable (do not change) list of data. List of constants

# name = "Zach"
# print(name)
# name = "Tim"
# print(name)
# ^ replacing name altogether, so it functions as a change.
# 
# name[1] = a
# print(name)
# ^ does not work because a string is immutable. Just need to replace the whole thing

#tuples are created with tuple_var_name = (value)
states = ('IL', 'IN', 'KY')

#print individual items
print (states[1])

#display multiple items in a tuple, use for in
for state in states:
    print(state)

# "modify" a tuple, we can combine them
states2 = ('FL', 'NY')
states = states + states2
print(states)