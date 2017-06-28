# encoding = utf-8

stationFile = open("C:\\Users\\wbl\\Desktop\\转发：所有收费站（添加省代码）\\天津市经纬度.txt", 'r', encoding='utf-8')
dataFile = open("C:\\Users\\wbl\\Desktop\\转发：所有收费站（添加省代码）\\201704收费站出入车流量.csv", 'r')
targetFile = open("C:\\Users\\wbl\\Desktop\\转发：所有收费站（添加省代码）\\201704整理.txt", 'w', encoding='utf-8')

stationDict = {}
for eachLine in stationFile:
    line = eachLine.strip()
    field = line.split(',')
    stationName = field[0]+field[1]
    content = line
    stationDict.setdefault(stationName, content)
    #print(line)

for eachLine in dataFile:
    line = eachLine.strip()
    field = line.split(',')
    stationName = field[1]
    stationNameIn = field[1] + '入'
    stationNameOut = field[1] + '出'
    contentIn = ''
    contentOut = ''
    for i in range(1, 31):
        contentIn += field[2*i+1] + ','
        contentOut += field[2*i] + ','
    if stationNameIn in stationDict.keys():
        contentIn = stationDict.get(stationNameIn) + ',' + contentIn
        contentIn = contentIn[:-1]
        targetFile.write(contentIn + '\n')
        print(contentIn)
    if stationNameOut in stationDict.keys():
        contentOut = stationDict.get(stationNameOut) + ',' + contentOut
        contentOut = contentOut[:-1]
        print(contentOut)
        targetFile.write(contentOut + '\n')

dataFile.close()
stationFile.close()
targetFile.close()

