import re
n = input()
con2 = re.findall(r"\d{2,}", n) # по факту он всё проверил
if len(con2):
    print(*con2) 
else:
    print()    
    