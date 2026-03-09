import re 
n = input()
txt = re.findall("[0-9]", n)
print(*txt)