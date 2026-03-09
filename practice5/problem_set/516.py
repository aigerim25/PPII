import re
user_input = input()
pattern = r"^Name:\s([A-Za-z]+(?:\s[A-Za-z]+)?),\sAge:\s(\d+)"
matching = re.fullmatch(pattern, user_input)
if matching:
    print(matching.group(1), matching.group(2))
else:
    print()  

