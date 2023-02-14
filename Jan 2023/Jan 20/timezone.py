from dateutil import tz
from datetime import datetime
aus_time = tz.gettz('Australia/Melbourne')
now = datetime.now()
#print(now)
#now_in_austr = now.astimezone(aus_time)
#print(now_in_austr)

sec_date = datetime(year=2022, month=9, day=23, hour=18, minute=21, tzinfo=tz.gettz('America/Los Angeles'))
# we create specific datetime object and specify timezone for it in tzinfo parameter


print(sec_date)
#print(sec_date.tzname())

ber_time = tz.gettz('Europe/Berlin')  # create variable what store Berlin timezone
converted_to_ber = sec_date.astimezone(ber_time)  # convert datetime object to specific timezone
print(converted_to_ber)


