def calc(expression):
    expression = expression.upper().strip()
    str_num = {
        "ONE":"1",
        "TWO":"2",
        "THR":"3",
        "FOU":"4",
        "FIV":"5",
        "SIX":"6",
        "SEV":"7",
        "EIG":"8",
        "NIN":"9",
        "ZER":"0"
    }
    num_str = {}
    for k, v in str_num.items():
        num_str[v] = k
    def words_to_number(word_string):
        number = ""
        for i in range(0, len(word_string), 3):
            chunk = word_string[i:i+3]
            number += str_num[chunk]
        return int(number)
    if "+" in expression:
        left, right = expression.split("+")
        result = words_to_number(left.strip()) + words_to_number(right.strip())
    elif "*" in expression:
        left, right = expression.split("*")
        result = words_to_number(left.strip()) * words_to_number(right.strip())
    elif "-" in expression:
        left, right = expression.split("-")
        result = words_to_number(left.strip()) - words_to_number(right.strip())

    result_str = ""
    for digit in str(result):
        result_str += num_str[digit]
    return result_str

exp = input()
print(calc(exp))    


