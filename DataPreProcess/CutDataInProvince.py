# encoding=utf-8


import os
from itertools import islice

from DataPreProcess.Function import *

# from PassRecord import *


stationPath = 'C:\\Users\\wbl\\Desktop\\ETC\\shandongStation.txt'

f = Function(stationPath)
f.setProvinceList()


rootDirName = "C:\\Users\\wbl\\Desktop\\ETC\\山东数据\\山东数据\\省内交易数据"
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
        for eachLine in islice(currentFile, 1, None):                        # 去除第一行
            line = eachLine.strip().decode('utf-8', 'ignore')
            field = line.split(',')
            date = field[0][16:20]
            if not field[7] == '000000000' and Function.judgeMonth(date):    # 确认是省内数据和四月份
                if len(field) == 54:                                         # 对数据进行处理
                    data = field[50].split(' ')
                    dateIn = data[0].replace('.', '').replace('-', '')
                    stationInBefore = data[1].split('，')[0]
                    stationIn = stationInBefore[:stationInBefore.find("站入")]
                    dateOut = data[1].split('，')[1].replace('.', '').replace('-', '')
                    stationOutBefore = data[2]
                    stationOut = stationOutBefore[:stationOutBefore.find("站出")]
                    transInfo = field[52].split('|')
                    # plateColor = transInfo[1]
                    plateNum = transInfo[2]
                    vehicleType = transInfo[3]
                    fee = float(field[44]) + float(field[45])
                    if f.judgeStation(stationIn) and f.judgeStation(stationOut):
                        line = dateIn + ',' + stationIn + ',' + dateOut + ',' + stationOut + ',' + str(fee) + ',' \
                               + plateNum + ',' + vehicleType
                        print(line)
                        writeDict[date].write(line + '\n')

                # print line
                # print date
                # writeDict[date].write(line + '\n')

        currentFile.close()

for key in writeDict.keys():
    writeDict[key].close()
