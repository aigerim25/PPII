#1 
students = [("Emil", 25), ("Tobias", 23), ("Linus",28)]
sorted_students = sorted(students, key=lambda a:a[1])
print(sorted_students)
#2 
words = ["apple","cherry","banana","watermelon","pie"]
sorted_words = sorted(words,key=lambda a:len(a)) # use key for custom sorting
print(sorted_words) 