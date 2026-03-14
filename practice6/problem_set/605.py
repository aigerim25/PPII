s = input().lower()
vowels = "aeiou"
if any(c in vowels for c in s):
    print("Yes")
else:
    print("No")    