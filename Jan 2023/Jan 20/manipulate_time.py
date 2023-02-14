
#TASK 1
#Using the variable called current_datetime, subtract 15 days from the current time.

#Hint: use .strftime() method to reformat the time

#If today is 8/07/2021, your result should look like this: 2021-06-23

from datetime import datetime, timedelta

current_datetime = datetime.now()
date = datetime.strptime("2021-07-08", "%Y-%m-%d")
fithin_days_earlier = date - timedelta(days=15)
print(fithin_days_earlier.strftime("%Y-%m-%d"))


#Task 2
#Using the variable called current_datetime, add 7 days to your current day.

#Your result should look like this, if today is 8/07/2021:
#2021-07-15

current_datetime = datetime.now()
date = datetime.strptime("2021-07-08", "%Y-%m-%d")
seven_days_later = date + timedelta(days=7)
print(seven_days_later.strftime("%Y-%m-%d"))


#Task 3
#Your task is to write a reminder message for a customer that is being sent out on 2020-01-01 to please pay in 25 days. Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.

#Steps:

#Start by creating a datetime of the current date, January 1st, 2020: current_date = datetime(year=2020, month=1, day=1)

#Do your calculations to add 25 days to current_date. Create a string and print it out. Your result should look like this:

#Hello Friedrich, your rent of 300 € is due on 26 January, 2020.



current_date = datetime(year=2020, month=1, day=1)
due_date = current_date + timedelta(days=25)
message = "Hello Friedrich, your rent of 300 € is due on "+due_date.strftime("%d %B, %Y")
print(message)