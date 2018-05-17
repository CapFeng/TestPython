# encoding=utf-8
import datetime

file1 = "C:\\Users\\wbl\\Desktop\\ETC\\totalNewSHK\\济南西.txt"
fileF1 = open(file1, 'r')

Day = range(20160405, 20160424, 1)
Hour = range(0, 24, 1)


def getSlideDate(dateString, hour):
    currentDate = datetime.datetime.strptime(dateString, '%Y%m%d%H')
    delta = datetime.timedelta(hours=hour)
    slideDate = currentDate - delta
    return slideDate.strftime('%Y%m%d%H')


countDict = {}
totalDict = {}

for eachLine in fileF1:
    field = eachLine.strip().split('\t')
    key = field[0]
    value = field[1]
    countDict.setdefault(key, value)
fileF1.close()

for (key, value) in countDict.items():
    valueArray = []
    tempArray = []
    for hour in range(1, 6):
        currentKey = getSlideDate(key, hour)
        tempArray.append(countDict.get(currentKey))
    valueArray.append(tempArray)
    totalDict.setdefault(key, valueArray)

file2 = "C:\\Users\\wbl\\Desktop\\ETC\\weatherData.txt"
fileF2 = open(file2, 'r')

for eachLine in fileF2:
    field = eachLine.strip().split('\t')
    date = field[0]
    del field[0]
    for i in range(0, 24):
        key = date + str(i).zfill(2)
        valueArray = totalDict.get(key)
        valueArray.append(field)
        totalDict.setdefault(key, valueArray)
fileF2.close()

fileTop1 = "C:\\Users\\wbl\\Desktop\\ETC\\totalNewSHK\\京台鲁冀.txt"
fileF31 = open(fileTop1, 'r')

countDict31 = {}
for eachLine in fileF31:
    field = eachLine.strip().split('\t')
    key = field[0]
    value = field[1]
    countDict31.setdefault(key, value)
fileF31.close()

for (key, value) in countDict31.items():
    tempArray = []
    for hour in range(1, 6):
        currentKey = getSlideDate(key, hour)
        tempArray.append(countDict31.get(currentKey))
    valueArray = totalDict.get(key)
    valueArray.append(tempArray)
    totalDict.setdefault(key, valueArray)

fileTop2 = "C:\\Users\\wbl\\Desktop\\ETC\\totalNewSHK\\青银鲁冀.txt"
fileF32 = open(fileTop2, 'r')

countDict32 = {}
for eachLine in fileF32:
    field = eachLine.strip().split('\t')
    key = field[0]
    value = field[1]
    countDict32.setdefault(key, value)
fileF32.close()

for (key, value) in countDict32.items():
    tempArray = []
    for hour in range(1, 6):
        currentKey = getSlideDate(key, hour)
        tempArray.append(countDict32.get(currentKey))
    valueArray = totalDict.get(key)
    valueArray.append(tempArray)
    totalDict.setdefault(key, valueArray)

fileTop3 = "C:\\Users\\wbl\\Desktop\\ETC\\totalNewSHK\\京台鲁苏.txt"
fileF33 = open(fileTop3, 'r')

countDict33 = {}
for eachLine in fileF33:
    field = eachLine.strip().split('\t')
    key = field[0]
    value = field[1]
    countDict33.setdefault(key, value)
fileF33.close()

for (key, value) in countDict33.items():
    tempArray = []
    for hour in range(1, 6):
        currentKey = getSlideDate(key, hour)
        tempArray.append(countDict33.get(currentKey))
    valueArray = totalDict.get(key)
    valueArray.append(tempArray)
    totalDict.setdefault(key, valueArray)

fileTop4 = "C:\\Users\\wbl\\Desktop\\ETC\\totalNewSHK\\泰安西.txt"
fileF34 = open(fileTop4, 'r')

countDict34 = {}
for eachLine in fileF34:
    field = eachLine.strip().split('\t')
    key = field[0]
    value = field[1]
    countDict34.setdefault(key, value)
fileF34.close()

for (key, value) in countDict34.items():
    tempArray = []
    for hour in range(1, 6):
        currentKey = getSlideDate(key, hour)
        tempArray.append(countDict34.get(currentKey))
    valueArray = totalDict.get(key)
    valueArray.append(tempArray)
    totalDict.setdefault(key, valueArray)


writeName = "C:\\Users\\wbl\\Desktop\\KDDCup\\NN.txt"

wirteFile = open(writeName, 'w', encoding='utf-8')
for (key, value) in totalDict.items():
    result = []
    resStr = ""
    for i in range(0, 6):
        result.extend(value[i])
    for i in range(0,len(result)):
        resStr += str(result[i])
        resStr += ','
    wirteFile.write(str(key)+','+resStr+countDict.get(key)+'\n')
wirteFile.close()

