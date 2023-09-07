#what is a class: a blueprint for an object that contains some data (attribute/field) and functions (methods)
#objects are instance of a class that contains data and functions
#instance - copy or spawn. Concrete copy that is generated by a class. An object is ver flexible in that it can be made to look a variety of ways
#objects are supposed to represent some type of concrete thing in the real world (or in game design some type of game object)

#to use a class we must first define it (like a function)
class MyClass:
    #attributes - aka variables within the class
    x = 5

#classes are supposed to be like blueprints. We can use variables within a class to be copied into a new instance of the class every time we create a new instance of the class

instance1 = MyClass() #creates an instance of MyClass (copy)
print(instance1.x) #access our attributes using dot(.) notation

instance2 = MyClass()
instance2.x = instance2.x - 1
print(instance2.x)
