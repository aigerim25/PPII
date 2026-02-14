#1 
def my_function(*kids): # args == tuple
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")    
#2 
def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)
my_function("Emil", "Tobias", "Linus")   
#3 kwargs returns dictionary
def my_function(**myvar): 
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
my_function(name = "Tobias", age = 30, city = "Bergen")    
#4 
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")    

