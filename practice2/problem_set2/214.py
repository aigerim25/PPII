n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
freq_num = numbers[0]
count = 0
for i in range(n):
    current_count = numbers.count(numbers[i])
    if current_count > count:
        count = current_count
        freq_num = numbers[i]
print(freq_num)        