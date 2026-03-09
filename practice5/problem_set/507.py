import re 
st = input().strip()
p = input().strip()
r = input().strip()
print(re.sub(p, r, st))
