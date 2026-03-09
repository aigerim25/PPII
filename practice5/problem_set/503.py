import re
s = input()
p = input()
match = re.findall(s,p)
if re.search(p,s):
    print(len(match))

          
    