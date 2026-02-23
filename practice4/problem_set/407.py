# str = input()
# rev = ''.join(reversed(str))
# print(rev)
str = input()
it = iter(reversed(str))
for ch in it:
    print(ch, end="")