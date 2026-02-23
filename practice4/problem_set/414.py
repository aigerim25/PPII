from datetime import datetime
input1 = input()
input2 = input()
date1 = datetime.strptime(input1, "%Y-%m-%d UTC%z")
date2 = datetime.strptime(input2, "%Y-%m-%d UTC%z")
diff = date1 - date2 
delta = abs(diff.total_seconds())
result = int(delta / 86400)
print(result)