from datetime import datetime
from dateutil.parser import parse

now = datetime.now()
parse('20160430')

print(parse('20160430'))

stamp = datetime(2017, 5, 4)

print(stamp.strftime('%Y-%m-%d'))

s = '040106'
print(s[0:4])
print(s[4:6])
day = []
for i in range(401, 431):
    day.append(str(i).zfill(4))

print(day)