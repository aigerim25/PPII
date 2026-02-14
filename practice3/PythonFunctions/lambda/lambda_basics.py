#1 
x = lambda a : a + 10 # он может принимать несколько аргументов, но у него только one expression/условие
print(x(5))
#2 
x = lambda a,b:a*b 
print(x(5,6))
#3 
def my_function(n):
    return lambda a:a*n
my_doubler = my_function(2) 
my_tripler = my_function(3)

print(my_doubler(11))
print(my_tripler(22))