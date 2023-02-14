from datetime import datetime


#TASK 1
current_time = datetime.now()
current_time = current_time.replace(year=2014)
print(current_time.year)

#TASK 2


some_date = datetime(year=2021, month=7, day=14)
week_day = some_date.weekday()
print(week_day)

# Task 3

year = 2024

if year %4==0:
    print(year , 'is a leap year')
else:
    print(year , 'is a not leap year')


# Task 4

user = input("Enter your time in the format 'MM DD YYYY HH:MMAM/PM': ")
user_time = datetime.strptime(user, '%b %d %Y %H:%M%p')
print(user_time)
