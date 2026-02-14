#1 
def my_function(fname): # fname - > it is our parameter 
    print(fname + " Refsnes")
my_function("Alex") # "Alex" or "Emil" they are our argument. это конкретные значение, которые мы даем при вызове функции 
my_function("Emil")    
#2 
def my_function(fname, lname): # we tell 2 arguments 
    print(fname + " " + lname) 
my_function("Emil", "Refsnes")    # and we should get two arguments
#3 
def my_function(name="friend"):
    print("Hello", name)
my_function("Aigerim")
my_function() # get default value "friend"
my_function("Emil")    
#4 
def my_function(animal,name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Barsik")    # key = value 
#5
def my_function(animal,name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
my_function("dog","Barsik") # можем написать так, но тут порядок параметров важен, как они написаны до вызова, так и должны они получить данные при выходе