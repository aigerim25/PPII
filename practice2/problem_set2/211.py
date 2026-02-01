n,l,r = map(int,input().split(  ))
numbers = list(map(int,input().split()))
before_l = numbers[:l-1]
after = numbers[r:]
interval = numbers[l-1:r]  
reversed_numbers = interval[::-1]
print(*(before_l + reversed_numbers + after))    
    
   
    
    
