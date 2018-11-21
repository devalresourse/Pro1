import time
import calendar

cal = calendar.month(2018,11,12)
clock = time.asctime(time.localtime(time.time()))
print (cal)
print(clock)
