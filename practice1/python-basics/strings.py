#1 multiline strings
a = """hello, my name is Aigerim.
Welcome to my github."""
print(a)
#2 
b = "Hello, world!"
print(b[2:6])
print(b[:6]) # there we dont have exact position like 2, so we start from the first character
print(b[2:]) # there otherwise from position 2 to till the end
print(b[-8:-3]) # начинаем с -1 с конца. [точка старта:точка стопа], но точка стопа не включительна, а точка старта включительна
#slicing string - начинаем с нулевого индекса. it is get characters from position 2 to position 6(not included 6)
#так же в счет идут , ! и другие знаки. пробел так же считается символом и его так же считаем
#3 
a = "the piece of wolrd"
print(a.upper())
print(a.lower())
print(a.replace("H", "K")) # we replace H with K. a.replace(character that we need to replace, character for which we need to replace)
print(a.split()) # делит один sentance на каждое слово 
#4 
age = 19
txt = f"Hello, I`m {age}"
#txt = f"Hello, I`m {9+9}"
print(txt)
#5
#txt = "Hello\nWorld!" #new line
txt = "Hello\tWorld"
print(txt)

