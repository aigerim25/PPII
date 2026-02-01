n = int(input())
numbers = list(map(int,input().split()))
max_value = max(numbers)
min_vlaue = min(numbers)
for i in range(len(numbers)):
    if numbers[i]==max_value:
        numbers[i]=min_vlaue
print(*numbers)        