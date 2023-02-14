import calendar

yy = 2023
mm = 11

month_calendar = calendar.month(yy, mm)  # create month calendar
#print(month_calendar)


year_calendar = calendar.calendar(2016)
#print(year_calendar)

print(calendar.isleap(2024))    # returns boolian TRUE or FALSE

calendar.setfirstweekday(3)
print(calendar.calendar(2016))