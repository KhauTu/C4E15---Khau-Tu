import datetime
now = datetime.datetime.now()
today = now.date()
moment = now.time()

print(now.year, now.month, now.day, now.hour, now.minute, now.second)
my_time = datetime.time(now.hour, now.minute, now.second)
print(my_time)
