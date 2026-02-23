import datetime 
import math 
def parsetoutc(date_str):
    parts = date_str.split()
    date_part = parts[0]
    timezone_p = parts[1]
    
    y,m,d = map(int, date_part.split('-'))
    dt = datetime.datetime(y,m,d,0,0,0, tzinfo=datetime.timezone.utc)
    sign = 1 if timezone_p[3] == "+" else -1 
    h, mins = map(int, timezone_p[4:].split(':'))
    offset_seconds = sign * (h * 3600 + mins * 60)
    return dt.timestamp() - offset_seconds
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def birthday(birth_month, birth_day, target_year):
    if birth_month == 2 and birth_day == 29:
        if not leap_year(target_year):
            return target_year, 2, 28
    return target_year, birth_month, birth_day
def solve():
    try:
        import sys
        input_data = sys.stdin.read().splitlines()
        if len(input_data) < 2:
            return
        birth_line = input_data[0].strip()
        current_line = input_data[1].strip()

        bdate = birth_line.split()[0]
        by, bm, bd = map(int, bdate.split('-'))
        btz = birth_line.split()[1]
        current_utc = parsetoutc(current_line)
        cy = int(current_line.split('-')[0])
        results = []
        for year in [cy, cy + 1]:
            ry, rm, rd = birthday(bm, bd, year)
            bday_str = f"{ry:04d}-{rm:02d}-{rd:02d} {btz}"
            butc = parsetoutc(bday_str)
            delta = butc - current_utc
            if delta >= 0:
                days = math.ceil(delta / 86400)
                print(int(days))
                return 
    except EOFError:
        pass            
if __name__ == "__main__":
    solve()                                        