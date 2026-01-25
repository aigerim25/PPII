#1 
x = 5
y = "hi"
print(x)
print(y)
#2
print(type(x))
print(type(y))
#3 
x = y = z = "Orange"
print(x,y,x)
#4 
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#5
x = "awesome"
def myfunc():
    x = "fantastic" 
    print("Python is " + x)
myfunc() 
print("Python is " + x)