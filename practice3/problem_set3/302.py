n = int(input())
count = 0
for d in (2,3,5):
    while n % d == 0:
        n //= d
        count += 1
if n == 1 and count >= 2:
    print("Yes")
else:
    print("No")            