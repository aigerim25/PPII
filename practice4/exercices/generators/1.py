import math
n = int(input())
nums = (i for i in range(1,n+1))
#print(nums)
for n in nums:
    print(int(math.pow(n,2)),end = " ")
