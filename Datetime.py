datetime
Python has the datetime module to help deal with timestamps in your code. Time values are represented with the time class. Times have attributes for hour, minute, second, and microsecond. They can also include time zone information. The arguments to initialize a time instance are optional, but the default of 0 is unlikely to be what you want.


time
Lets take a look at how we can extract time information from the datetime module. We can create a time-stamp by specifying datetime.time(hour,minute,second,microsecond)

In [3]:
import datetime

t = datetime.time(4, 20, 1)
# Lets show the different compoenets

print t
print 'hour  :', t.hour
print 'minute:', t.minute
print 'second:', t.second
print 'microsecond:', t.microsecond
print 'tzinfo:', t.tzinfo
04:20:01
hour  : 4
minute: 20
second: 1
microsecond: 0
tzinfo: None
Note: A time instance only holds values of time, and not a date associated with the time.


We can also check the min and max values a time of day can have in the module:

In [5]:
print 'Earliest  :', datetime.time.min
print 'Latest    :', datetime.time.max
print 'Resolution:', datetime.time.resolution
Earliest  : 00:00:00
Latest    : 23:59:59.999999
Resolution: 0:00:00.000001
The min and max class attributes reflect the valid range of times in a single day.
