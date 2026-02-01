x = int(input())
s = set() # создали set, потому что он как раз нам нужен чтобы не считать дубликаты в инпутах 
for i in range(x):
    inputs = input()
    s.add(inputs)   
print(len(s))    