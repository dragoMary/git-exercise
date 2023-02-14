

#If today is 8/07/2021, your result should look like this: 2021-06-23
'''
from datetime import datetime, timedelta

def get_date_15_days_earlier(input_date):

    date = datetime.strptime(input_date, "%Y-%m-%d")
    fifteen_days_earlier = date - timedelta(days=15)
    return fifteen_days_earlier.strftime("%Y-%m-%d")

print(get_date_15_days_earlier("2021-07-08"))

'''

'''
import calendar

def print_calendar(year, month):
    month_calendar = calendar.month(year, month)
    print(month_calendar)
    year_calendar = calendar.calendar(2016)
    print(year_calendar)
    print(calendar.isleap(year))
    calendar.setfirstweekday(3)
    print(calendar.calendar(year))

print_calendar(2016, 12)

'''

# a reminder message for a customer that is being sent out on 2020-01-01
#Start by creating a datetime of the current date, January 1st, 2020: current_date = datetime(year=2020, month=1, day=1)
from datetime import datetime, timedelta

def reminder(name, amount, due_days, current_date=datetime.now()):
   due_date = current_date + timedelta(days=due_days)
   reminder = "Hello " + name + ", your rent of " + str(amount) + " € is due on " + due_date.strftime("%d,%B, %Y")
   print(reminder)



reminder("Friedrich", 300, 25)
reminder("John", 500, 10,datetime(year=2020, month=2, day=1))
reminder("Sigfid", 100, 12)



'''

def string(text):
    return lambda any: f'{text}, {any}'
text = 'Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburgs capital.'
print(text.replace('capital', 'capital of Germany'))

'''

'''
def city ():
    return city()

population = 3645000
city = 'berlin'
print(city.capitalize(), 'has a population of:', population)

'''
'''
def text():
    text = 'Berlin is a world city of culture, politics, media and science.'
    return text
    
print(len(text()))

'''

