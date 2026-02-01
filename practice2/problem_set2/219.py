n = int(input())
doramas = {}
for i in range(n):
    data = input().split()
    name = data[0]
    count = int(data[1])

    if name in doramas:
        doramas[name] = doramas[name] + count
    else:
        doramas[name] = count
names_list = list(doramas.keys())
names_list.sort()
for name in names_list:
    print(name, doramas[name])            