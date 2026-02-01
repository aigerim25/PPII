#1 
a = 5 
b = 3
if a > b: print("a is greater than b")
#2 
a = 2 
b = 330 
print("A") if a > b else print("B")
#3 
a = 10
b = 20
bigger = a if a > b else b 
print("Bigger is", bigger)
#4 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 
#print A if a > b 
#print = if a == b
#else print B, то есть когда мы пишем вот так сокрвщенно, то использовать elif не можем 
#5 
x = 15 
y = 20 
max_value = x if x > y else y # это читается как передай значение x в max_value если x > y 
print("Max value: ", max_value)