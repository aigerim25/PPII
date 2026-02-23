from datetime import datetime
x = datetime.now().replace(microsecond = 0) # drop microsecond
print(x)