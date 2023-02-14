from datetime import datetime

def extract_birthday(date_str):

    date = datetime.strptime(date_str, "%Y-%m-%d")
    current_year = datetime.now().year
    birthday = date.replace(year=current_year)
    return birthday

date_str = "1980-04-11"
birthday = extract_birthday(date_str)
print(birthday)



#Task 5

import datetime

def day_difference(first_birthday, second_birthday):
    first_birthday_date = datetime.datetime.strptime(first_birthday, '%Y-%m-%d')
    second_birthday_date = datetime.datetime.strptime(second_birthday, '%Y-%m-%d')
    difference = (first_birthday_date - second_birthday_date).days
    return difference

first_birthday = "1980-04-11"
second_birthday = "1970-06-11"
difference = day_difference(first_birthday, second_birthday)
print('number of days between two birthdays:', difference)



#Task 1: weekday of birthday

from datetime import datetime
import calendar
def get_weekday(date_string):
    date = datetime.strptime(date_string, '%Y-%m-%d')

    week = calendar.day_name[date.weekday()]
    print('the weekname is:', week)
    return date.weekday()
weekday = get_weekday("1236-04-11")
print('the weekday is:', weekday)


#Number of Sundays since a birthdate

from datetime import datetime, timedelta
import calendar

def count_sundays(date_string):
    birthdate = datetime.strptime(date_string, "%Y-%m-%d")
    current_date = datetime.now()
    delta = current_date - birthdate
    sundays = 0
    for i in range(delta.days):
       if (birthdate + timedelta(i)).weekday() == calendar.SUNDAY:
           sundays += 1

    return sundays

sundays = count_sundays("2022-04-11")
print('nr. of sundays since birthdate:', sundays)


