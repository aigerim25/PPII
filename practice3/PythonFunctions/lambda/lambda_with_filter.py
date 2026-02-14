#1 
numbers = [1,2,3,4,5,6] 
odd_numbers = list(filter(lambda a:a%2!=0,numbers))
print(*odd_numbers)
#2 
numbers = list(map(int,input().split())) 
even_number = list(filter(lambda a:a%2==0,numbers)) # выводит, если результат приводится к True 
print(*even_number)
