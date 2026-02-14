class LambdaOperations: 
    def __init__(self, numbers):
        self.numbers = numbers
    def Abs(self):
        self.numbers = list(map(lambda a: abs(a), self.numbers))
    def Add(self,k):
        self.numbers = list(map(lambda a: a + k, self.numbers))
    def Multiply(self,k):
        self.numbers = list(map(lambda a: a * k, self.numbers))
    def Power(self,k):
        self.numbers = list(map(lambda a: a ** k, self.numbers))
n = int(input())
numbers = list(map(int,input().split()))
numOp = int(input())
calc = LambdaOperations(numbers)
for i in range(numOp):
    name_count = input().split()
    if name_count[0] == "abs":
        calc.Abs()
    elif name_count[0] == "add" :
        calc.Add(int(name_count[1]))
    elif name_count[0] == "multiply":
        calc.Multiply(int(name_count[1]))
    elif name_count[0] == "power":
        calc.Power(int(name_count[1]))
print(*calc.numbers)            







        








