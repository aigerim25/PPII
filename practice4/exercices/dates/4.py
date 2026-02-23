from datetime import datetime, date
input1 = input()
input2 = input()

dt1 = datetime.strptime(input1, "%Y-%m-%d").date()
dt2 = datetime.strptime(input2, "%Y-%m-%d").date()
diff = dt1 - dt2
print(diff.total_seconds()) #чтобы вывести результат в секундах 