#lists are mutable collections (multiple data types) where the elements can be modified, added to, or deleted.

test_scores = [90,70,75,54,90]

#items are elements, placement is their index starting with 0

print(test_scores[0])
print(test_scores[3])

#display all items in a list and/or manipulate element values
#for in loop - for items in the list
#the score variable below is a placeholder for each individual score in the list

for score in test_scores:
    score = score - 2
    print(score)

#append (add) data to a list
new_score = 95
test_scores.append(new_score)
print(test_scores)

#extend combines data from one list to another
test_scores2 = [100, 55]
test_scores.extend(test_scores2)
print(test_scores)

#remove data from a list using remove fuction/method
test_scores.remove(55)
print(test_scores)

#find something in a list to remove
looking_for = int(input("Give me a number you want to remove from a list: "))
found = looking_for in test_scores
if found == True:
    test_scores.remove(looking_for)
    print("FOUND")
    print(test_scores)
else:
    print("Value is not in list")

#count instances of something use count function/method
print(test_scores.count(90))

#sorting list using sort function
test_scores.sort()
print(test_scores)

#finding the length of a list buy using the len function
print(len(test_scores))