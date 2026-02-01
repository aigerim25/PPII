#1 
print(10>9)
print(1>2)
#2
print(bool("Hello"))
print(bool(15))
#3 
x = "Hello"
y = 15 
print(bool(x))
print(bool(y))
#4
x = bool(())
y = bool(None)
print(x,y)
#5 
print(bool({}))
#if string будет non-empty, то тогда вывод будет True
#if string empty, 0, (), {}, "", то тогда вывод False  
