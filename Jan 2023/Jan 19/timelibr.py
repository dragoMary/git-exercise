
import time

my_time = time.time()
#print(my_time)
#print(time.ctime(my_time))  #string
my_local_time = time.localtime(my_time)  #tuple with daytime info

#print('this is printed now')
#time.sleep(3)
#print('this will be printed out in 3 sec')
my_utc_time = time.gmtime(my_time)    # UTC time
print(my_local_time)
print(my_utc_time)
user_time = time.strftime('%d %Y %m %H%M%S', my_local_time)
print(user_time)
print(time.strftime('Today: %A %y %B Time: %I:%M:%S %p', my_local_time))

result = time.strptime('13 Jan 2021', '%d %b %Y')
print(result)



