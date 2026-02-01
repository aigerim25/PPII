x = int(input())
numbers = list(map(int,input().split()))
m = max(numbers)
idx = numbers.index(m)
print(idx + 1)

