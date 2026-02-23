def powerOfTwo(n):
    for i in range(n+1):
        yield 2**i
n = int(input())
for i in powerOfTwo(n):
    print(i, end=" ")        
