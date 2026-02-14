class Person:
    def __init__(self,name,gpa):
        self.name = name 
        self.gpa = gpa
    def get_info(self):
        return f"Student: {self.name}, GPA: {self.gpa}"
name, gpa = input().split()
gpa = float(gpa)
person = Person(name,gpa)
result = person.get_info()
print(result)        


