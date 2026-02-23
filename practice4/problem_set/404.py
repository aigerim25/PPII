import math
def squares(a,b):
    for i in range(a,b+1):
        yield i*i
a,b = list(map(int,input().split()))
for num in squares(a,b):
    print(num)       

