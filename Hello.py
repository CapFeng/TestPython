# encoding=utf-8
from dateutil.parser import parse
from datetime import datetime

'''
date = "2016-04-02"
print date.replace('-', '')[4:8]

for i in range(0, 20):
    Function.getVehicleType(str(i))

'''


str = "20160331163550"
str1 = '客1'
print(str1[0])
date = str[4:8]
hour = str[8:10]
#print(date, hour)

#date = parse('2016040501')
date = datetime.strptime('2016040501', '%Y%m%d%H')
#datetime.date()
#print(date)
'''

strsss = "诸城东站入"
print strsss[:strsss.find("站入")]
'''
'''
testString = "2016-04-30-21.08.23 诸城东站入，2016-04-30-23.53.11 沈海鲁苏站出 总重45.20吨 超限率0.0％"
data = testString.split(' ')
print data[0].replace('.', '').replace('-', '')
print data[1].split('，')[0]
print data[1].split('，')[1].replace('.', '').replace('-', '')
print data[2]
'''

'''
inIndex = testString.find("站入")
outIndex = testString.find("站出")
print testString[:19].replace('.', '').replace('-', '')
print testString[20:inIndex]
print testString[inIndex+9:inIndex+28]
print testString[inIndex+29:outIndex]
'''
'''
testString = "2000000,5,7,9999999937020001,9999999901020001,5671458,1,2016-03-30,9999999937030001,9999999911010001,5671458,125,11993.75,1,2016-03-30,13:55:17,47.5,1,马场,鲁北,1,04,3701,120106,91,20160330  135517,03,3701,130102,81,20160330  123624,22,1101,1201220001133204,京N4V408,318,580.75,533.25,A7B17BE7,09,01370000f3ab,000F8DC9,1101,1101120170463828,0001,京N4V408,toll"

line = testString.split(',')

index = 0
for word in line:
    print str(index) + ': ' + line[index]
    index += 1
'''

'''
stationpath = 'C:\\Users\\wbl\\Desktop\\ETC\\shandongStation.txt'

f = Function(stationpath)

f.setprovincelist()

str = '0123456789'
print str[0:3]


def month(monthstring):
    if int(monthstring) in range(401, 431):
        return True
    else:
        return False


print month("0430")
'''