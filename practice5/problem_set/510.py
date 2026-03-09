import re 
n = input()
checker_c = re.search("cat|dog", n)
if checker_c == None:
    print("No")
else:
    print("Yes")       
  
    
   
