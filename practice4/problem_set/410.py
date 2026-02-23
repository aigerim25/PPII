def repeat(string, k):
    nums = string.split()
    for i in range(k):
        for n in nums:
            yield n
string = input()
k = int(input())
for n in repeat(string,k):
    print(n,end=" ")        
