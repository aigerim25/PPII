sent = input()
target = input()
replace_word = input()
new_sent = sent.replace(target, replace_word)
if target in sent:
    print(new_sent)
else:
    print(sent)    
