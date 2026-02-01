n = int(input())
words = []
for i in range(n):
    words.append(input())
string = {}
for i in range(n):
    w = words[i]
    if w not in string:
        string[w] = i + 1
sorted_keys = sorted(string.keys())
for w in sorted_keys:
    print(w,string[w])            