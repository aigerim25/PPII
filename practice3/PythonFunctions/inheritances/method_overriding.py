#1 
class Person:
    def __init__(self,fname,lname):
        self.fname = fname 
        self.lname = lname 
    def printname(self):
        print(self.fname, self.lname)
class Student(Person):
    def __init__(self,fname,lname): # the child`s init function overrides the inheritance of parent`s init function 
        Person.__init__(self,fname,lname)
x = Student("Mike", "Own")
x.printname()
                