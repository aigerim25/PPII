class Pair:
    def __init__(self,a1,b1,a2,b2):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2 
    def a_sum(self):
        return a1 + a2
    def b_sum(self):
        return b1 + b2     
a1,b1,a2,b2 = map(int,input().split())
sum_of_a = Pair(a1,b1,a2,b2)
sum_of_b = Pair(a1,b1,a2,b2)
result_a = sum_of_a.a_sum()
result_b = sum_of_b.b_sum()
print("Result:", result_a, result_b)


