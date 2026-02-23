import math
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
per = l * n 
a = l / 2 * math.tan(math.radians(180/n))
area = (per * a) / 2
print("Expected Output: ", round(area))

