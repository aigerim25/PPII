x = int(input())
numbers = list(map(int,input().split()))
for x in numbers:
    power = pow(x,2)
    print(power, end=" ")        