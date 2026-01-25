#1 multiline strings
a = """hello, my name is Aigerim.
Welcome to my github."""
print(a)
#2 
b = "Hello, world!"
print(b[2:6])
print(b[:6]) 
print(b[2:]) 
print(b[-8:-3]) 
#3 
a = "the piece of wolrd"
print(a.upper())
print(a.lower())
print(a.replace("H", "K")) 
print(a.split())
#4 
age = 19
txt = f"Hello, I`m {age}"
#txt = f"Hello, I`m {9+9}"
print(txt)
#5
#txt = "Hello\nWorld!" #new line
txt = "Hello\tWorld"
print(txt)

