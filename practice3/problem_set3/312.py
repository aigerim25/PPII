class Employee:
    def __init__(self, emp_type, base_salary):
        self.emp_type = emp_type
        self.base_salary = base_salary
class Manager(Employee):
    def __init__(self, emp_type, name, base_salary, bonus):
        super().__init__(emp_type,base_salary) 
        self.name = name 
        self.bonus = bonus
    def forMng(self):
        total_salary = self.base_salary * (1 + self.bonus/100)
        print(f"Name: {self.name}, Total: {total_salary:.2f}")    
class Developer(Employee):
    def __init__(self, emp_type, name, base_salary, proj):
        super().__init__(emp_type,base_salary)
        self.name = name  
        self.proj = proj
    def forDev(self):
        total_salary = self.base_salary + self.proj * 500
        print(f"Name: {self.name}, Total: {total_salary:.2f}")
class Intern(Employee):
    def __init__(self, emp_type, name, base_salary):
        super().__init__(emp_type, base_salary)
        self.name = name
    def forInter(self):
        total_salary = self.base_salary
        print(f"Name: {self.name}, Total: {total_salary:.2f}")
user_data = input().split()
emp_type = user_data[0]
if emp_type == "Manager":
    name, base_salary, bonus = user_data[1], float(user_data[2]), int(user_data[3])
    mng = Manager(emp_type, name, base_salary, bonus)
    mng.forMng()
elif emp_type == "Developer":
    name, base_salary,proj = user_data[1],float(user_data[2]),int(user_data[3])
    dev = Developer(emp_type,name,base_salary,proj)
    dev.forDev()
elif emp_type == "Intern":
    name,base_salary = user_data[1],float(user_data[2])
    inter = Intern(emp_type,name,base_salary)
    inter.forInter()                                    

   






  

