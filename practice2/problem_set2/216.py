n = int(input())
numbers = list(map(int,input().split()))
s = set()
for x in numbers:
    if x in s:
        print("NO")
    else:
        print("YES")
        s.add(x)       

