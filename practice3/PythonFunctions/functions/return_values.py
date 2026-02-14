#1
def my_function(a,b):
    return a + b 
print(my_function(4,4))    
#2
def Square():
    a,b = map(int,input().split())
    return (a**2 + b**2)
print(Square())    
#3 
def get_greething():
    return "Hello, from a function"
print(get_greething())
