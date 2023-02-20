import datetime as dt

"""
Write a Python program to subtract five days from current date.
Write a Python program to print yesterday, today, tomorrow.
Write a Python program to drop microseconds from datetime.
Write a Python program to calculate two date difference in seconds.
"""

def minus5days():
    return dt.datetime.now() - dt.timedelta( days= 5)

def yesterTomor():
    yesterday = dt.datetime.now() - dt.timedelta( days= 1)
    today = dt.datetime.now()
    tomorrow = dt.datetime.now() + dt.timedelta( days= 1)
    return [yesterday, today, tomorrow]

def dropMicroSec( date):
    newdate = date.replace( microsecond = 0)
    return newdate

def diffenceSec( date1, date2):
    timedelta = dropMicroSec(date1)- dropMicroSec(date2)
    return abs(timedelta.total_seconds() )


print( minus5days() )
a, b, c = yesterTomor()
print( a, b, c)
data = dt.datetime( year = 2010, month = 12, day = 13, hour= 23, minute= 45, second= 56, microsecond= 1235)
print (dropMicroSec(data))

print( diffenceSec( data, dt.datetime.now()))