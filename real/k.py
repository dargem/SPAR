raw_month_to_day = {
    1 : 0,
    2 : 30,
    3 : 31,
    4 : 31,
    5 : 28,
    6 : 31,
    7 : 31,
    8 : 30,
    9 : 31,
    10: 31,
    11: 30,
    12: 31
}

month_to_day = {}

for val in raw_month_to_day.keys():
    days = 0
    for i in range(1, val + 1):
        days += raw_month_to_day[i]

    month_to_day[val] = days

data = input().split()
filt = [int(d) for d in data]

day, month, year = filt

# gonna be same year
actual_day = day + month_to_day[month]

real_day_to_month = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10: 31,
    11: 30,
    12: 31
}

for month, length in real_day_to_month.items():
    if actual_day <= length:
        print(f"{actual_day} {month} {year}")
        exit()

    actual_day -= length