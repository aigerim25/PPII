#1 
class MyClass: # we create class 
    x = 5 
p1 = MyClass() # create an object = p1 
print(p1.x)    
# del p1 -> "del" is the keyword used to delete an object
#2 
class MyClass:
    x = int(input())
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x) 
#3 
class Person:
    pass   # used to avoid getting an error 
    