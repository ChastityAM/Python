import time
import datetime

#print(datetime.datetime.year)
today = datetime.datetime.now()
print(today)
print(type(today))
print(f"year = {today.year}")
print(f"month = {today.month}")
print(f"day = {today.day}")
tz = datetime.timezone(datetime.timedelta(hours=5))





#time.time()
#time.gmtime()
#time.localtime()
#time.ctime()
print("going to sleep")
time.sleep(5)#pauses execution of your script for this many seconds

