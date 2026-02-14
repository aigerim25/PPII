#1
numbers = [1,2,3,4,5]
doubled = list(map(lambda x:x*2,numbers))
print(*doubled)
#2 
numbers = list(map(int,input().split()))
Square = list(map(lambda a:a**2,numbers))
print(*Square)
#3 
numbers = list(map(int,input().split()))
summ= list(map(lambda a:a+2,numbers)) 
print(*summ)