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
x = "awesome" # outside variable
def myfunc():
    x = "fantastic" # inside variable
    print("Python is " + x)

myfunc() # inside function output

print("Python is " + x) # outside function print
"""
"+" - это concetination, то есть two varibles will be printed as one word
"""