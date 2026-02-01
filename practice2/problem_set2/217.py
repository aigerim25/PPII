n = int(input())
counts = {}
for i in range(n):
    phone = input().strip()
    if phone in counts:
        counts[phone] += 1
    else:
        counts[phone] = 1
result = 0
for key in counts:
    if counts[key] == 3:
        result += 1 
print(result)                    