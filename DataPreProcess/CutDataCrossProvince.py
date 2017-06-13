# encoding=utf-8


import os
from DataPreProcess.Function import *
from itertools import islice
# from PassRecord import *


stationPath = 'C:\\Users\\wbl\\Desktop\\ETC\\shandongStation.txt'

f = Function(stationPath)
f.setProvinceList()


rootDirName = "C:\\Users\\wbl\\Desktop\\ETC\\山东数据\\山东数据\\跨省交易数据"
writeDirName = "C:\\Users\\wbl\\Desktop\\ETC\\Process"

writeDict = {}

for date in range(401, 431):
    date = str(date).zfill(4)
    dateFile = writeDirName + '\\' + date + '.txt'
    writeDict[date] = open(dateFile.decode('utf-8'), 'a')       # 请注意，此处是追加模式

    # print dateFile


for fileName in os.listdir(rootDirName.decode('utf-8')):
    if not os.path.isdir(fileName):
        currentFile = open(os.path.join(rootDirName, fileName), 'r')
        # writeFile = open(os.path.join(writeDirName, ), 'a')
        count = 0
        for eachLine in currentFile:
            line = eachLine.strip().decode('utf-8', 'ignore')
            field = line.split(',')
            date = field[14].replace('-', '')[4:8]
            if len(field) == 47 and Function.judgeMonth(date):                            # 确认是跨省数据数据
                dateIn = field[30].replace(' ', '')
                stationIn = field[18]
                dateOut = field[25].replace(' ', '')                                      # 跨省数据中，出入站时间是反的
                stationOut = field[19]
                plateNum = field[34]
                fee = field[16]
                vehicleType = Function.getVehicleType(field[20])
                if f.judgeStation(stationIn) or f.judgeStation(stationOut):
                    line = dateIn + ',' + stationIn + ',' + dateOut + ',' + stationOut + ',' + str(fee) + ',' \
                           + plateNum + ',' + vehicleType
                    print(line)
                    writeDict[date].write(line + '\n')

        currentFile.close()

for key in writeDict.keys():
    writeDict[key].close()
