import os
import datetime
def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)
r = modification_date('2.jpg')
s = modification_date('3.jpg')
print r
print s
