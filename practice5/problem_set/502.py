import re
s = input() # сама строка
p = input() # substring
if re.search(p, s):
    print("Yes")
else:
    print("No")    
