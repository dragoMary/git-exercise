#Task 1

#Use your birthday or a friend's
#Hint: use tz.gettz() method to setup the timezone.
#birthday = datetime(..., tzinfo=...)
#birthday_in_newzealand = birthday.astimezone(...)

from datetime import datetime
from dateutil import tz



german_tz = tz.gettz('Europe/Berlin')
#local time
birthday = datetime(year=1970, month=5, day=21, hour=15, minute=21, second=0, tzinfo=german_tz)
nz_tz = tz.gettz('Pacific/Auckland')  #time zone time

birthday_in_newzealand = birthday.astimezone(nz_tz)
print('birthday_in_germany',birthday,'birthday_in_newzealand', birthday_in_newzealand)


#Task 2

#Your team is a multinational one meeting a regional leader based in Moscow, Russia, with the following regions:

#Dublin / Ireland
#San Francisco / USA
#Berlin / Germany
#Johannesburg / South Africa
#Write a Python script that will print out the different times the teams will meet.


import datetime as dt
from dateutil import tz
from dateutil import relativedelta as datetime

moscow_tz = tz.gettz('Europe/Moscow')
meeting_time = dt.datetime(2021,8,7, 13, 35, tzinfo=moscow_tz)
#meeting_time = datetime(year=2021,month=8,day=7, minute=13, second=35)
meeting_time = dt.datetime.now()
ireland_tz = tz.gettz('Europe/Dublin')
sf_tz = tz.gettz('USA/San_Francisco')
berlin_tz = tz.gettz('Europe/Berlin')
johannesburg_tz = tz.gettz('Africa/Johannesburg')

# Convert the meeting time to the respective timezones
meeting_time_ireland = meeting_time.astimezone(ireland_tz)
meeting_time_sf = meeting_time.astimezone(sf_tz)
meeting_time_berlin = meeting_time.astimezone(berlin_tz)
meeting_time_johannesburg = meeting_time.astimezone(johannesburg_tz)

print(f"Irish participants will meet at: {meeting_time_ireland}")
print(f"German participants will meet at: {meeting_time_berlin}")
print(f"South African participants will meet at: {meeting_time_johannesburg}")
print(f"American participants will meet at: {meeting_time_sf}")




#Task 3

#Write a Python program to convert a UNIX timestamp like 1626430738 to a readable date

from datetime import datetime
timestamp = 1626430738
readable_date = datetime.fromtimestamp(timestamp)      # Convert the timestamp to a datetime object
print(readable_date.strftime("%m/%d/%Y, %H:%M:%S"))





