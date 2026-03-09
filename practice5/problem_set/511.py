import re 
n = input()
count_upp = re.findall("[A-Z]",n)
print(len(count_upp))    
