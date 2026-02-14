#1 parent class  
class Person:
    def __init__(self,fname,lname):
        self.fname = fname 
        self.lname = lname 
    def printname(self):
        print(self.fname, self.lname)
x = Person("John", "Doe")
x.printname()
#2 child class 
class Person:
    def __init__(self,fname,lname):
        self.fname = fname 
        self.lname = lname 
    def printname(self):
        print(self.fname, self.lname)
class Student(Person): # child class that inherits from Person class or parent class
    pass 
x = Student("Mike", "Own")
x.printname()           

