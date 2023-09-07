classmates = {'Tony':' cool but smells', 'Stacy':' Mom has got it going on', 'Emma':' Sits behind me', 'Lucy':' asks too many questions'}

print(classmates)
print((classmates)['Emma']) #print value of Emma

for k, v in classmates.items():
    print(k + v)


mycar = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for values in mycar:
    print(mycar[values])