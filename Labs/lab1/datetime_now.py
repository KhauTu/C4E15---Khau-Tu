# 1. import the datetime
import datetime
now = datetime.datetime.now()
today = now.date()
moment = now.time()

# 2. create a date and time objects
today = datetime.date.today()
moment = datetime.datetime.now().time()
now = datetime.datetime.combine(today, moment)

# 3. the timedelta object
yestorday = today - datetime.timedelta(1)

delta = yesterday -today

# 4.  Date objects have three mandatory arguments
my_date = datetime.date(1992, 3, 11)
my_date = datetime.date(day = 11, year = 1992, month = 3)

# 5.  Time objects don’t have mandatory arguments
my_time = datetime.time()
my_time = datetime.time(0, 0)
my_time = datetime.time(hour = 0, minute = 0)

# 6. Datetime objects have the same mandatory arguments as the date objects
my_datetime = datetime.time(year = 1992, month = 3, day = 11, hour = 4, minute = 15)

# 7. Change one datetime object to obtain another
another_datetime = my_datetime.replace(year = 1991, month = 10)

# 8. Obtain a datetime object representing the epoch: 01-01-1970
epoch = datetime.datetime.utcfromtimestamp(0)

# 9. Obtain the number of days and seconds between the epoch and now
delta = now - epoch
days = delta.days

seconds = delta.seconds
total_seconds = delta.total_seconds()

# 10. Recover now using the number of seconds since epoch using the utcfromtimestamp method
now = datetime.datetime.utcfromtimestamp(seconds)

# 11. Write a date object
string_date = str(my_date)

# 12. Recover a date object from a string
my_date = datetime.date(*[int(i) for i in string_date.split("-")])

# 13. Write a date object with a custom string format – the strftime method
string_date = my_date.strftime('%m/%d/%Y')

print(now.year, now.month, now.day, now.hour, now.minute, now.second)

my_time = datetime.time(2, 11)
print(my_time)
