import re 
n = input()
pattern = r"\S+@\S+\.\S+"
txt = re.search(pattern, n)
if txt == None:
    print("No email")
else:
    result = txt.group()
    print(result)             
         