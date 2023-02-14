import datetime

today = datetime.datetime.today()
#print(type(today))
#print(datetime.date.today())
#custom_datetime = datetime.date(year=2013, month=6, day=21)
#print(custom_datetime)
#print(datetime.date.fromisoformat('2022-01-13'))    #convert from str into date with iso
a = datetime.date.fromisoformat('2007-12-08')
#print(type(a))
#print(type(2))
b = datetime.datetime.fromisoformat('2020-02-14 12:43')
print(b)
# YYYY-MM-DD HH:MM:SS.mmmmm ISO 8601 date format

test_date = datetime.datetime(year=2001, month=6, day=25, hour=11, minute=5, second=54, microsecond=18 )
#print(test_date)

#user_date = test_date.strftime('%A, %d %B %Y %H:%M:%p')
#print(user_date)

tm_delta = datetime.timedelta(days=3)   # amount of days an user subscribe for a service (3 days)
date_with_delta = test_date + tm_delta
print(date_with_delta)

