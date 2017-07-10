# 天津市数据基本处理流程
# encoding = utf-8

stationFile = open("C:\\Users\\wbl\\Desktop\\转发：所有收费站（添加省代码）\\天津市经纬度.txt", 'r', encoding='utf-8')
dataFile = open("C:\\Users\\wbl\\Desktop\\转发：所有收费站（添加省代码）\\201704收费站出入车流量.csv", 'r')
targetFile = open("C:\\Users\\wbl\\Desktop\\转发：所有收费站（添加省代码）\\201704整理格式日期版.txt", 'w', encoding='utf-8')

stationDict = {}
for eachLine in stationFile:
    line = eachLine.strip()
    field = line.split(',')
    stationName = field[0]
    location = field[2] + ',' + field[3]
    if stationName not in stationDict.keys():
        stationDict.setdefault(stationName, location)

for eachLine in dataFile:
    line = eachLine.strip()
    field = line.split(',')
    stationName = field[1]
    contentIn = ''
    contentOut = ''
    writeString = ''
    for i in range(1, 31):
        contentIn = field[2*i+1]
        contentOut = field[2*i]
        date = '201704' + str(i).zfill(2)
        if stationName in stationDict.keys():
            writeString = stationName + ',' + stationDict.get(stationName) + ',' + date + ',' + contentIn + ',' + contentOut
            print(writeString)
            targetFile.write(writeString + '\n')


dataFile.close()
stationFile.close()
targetFile.close()

