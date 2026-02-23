n = int(input())
nums = (i for i in range(n+1))
for n in nums:
    if n % 2 == 0:
        print(n, end = " ") # n это уже числа