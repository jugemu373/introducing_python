# 13.1
from datetime import timedelta
from datetime import date

now = date.today()
now_str = now.isocalendar()
with open('today.txt', 'w') as output:
    print(now_str, file=output)


# 13.2
with open('today.txt', 'r') as input:
    today_string = input.read()

print(today_string)


# 13.3
# fmt = '%Y-%m-%d\n'
# print(date.strptime(today_string, fmt))


# 13.4
my_day = date(1996, 4, 23)
print(my_day)


# 13.5
print(my_day.weekday())
print(my_day.isoweekday())


# 13.6
party_day = my_day + timedelta(days=10000)
print(party_day)
