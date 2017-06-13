# encoding=utf-8

import os
import codecs
from DataPreProcess.PassRecord import *

rootDirName = "C:\\Users\\wbl\\Desktop\\ETC\\Process"


stationInDict = {}
stationOutDict = {}

for fileName in os.listdir(rootDirName.decode('utf-8')):        # 打开所在文件夹
    if not os.path.isdir(fileName):
        currentFile = open(os.path.join(rootDirName, fileName), 'r')
        for eachLine in currentFile:
            line = eachLine.strip().decode('utf-8', 'ignore')
            field = line.split(',')
            if len(field) == 7:
                record = PassRecord(field[1], field[3], field[0], field[2], field[4], field[6], field[5])
                stationIn = record.stationIn
                stationOut = record.stationOut
                print(stationIn + "----" + stationOut)
                if stationIn not in stationInDict.keys():
                    stationInDict.setdefault(stationIn, [record])
                elif stationIn in stationInDict.keys():
                    stationInDict.get(stationIn).append(record)
                if stationOut not in stationOutDict.keys():
                    stationOutDict.setdefault(stationOut, [record])
                elif stationOut in stationOutDict.keys():
                    stationOutDict.get(stationOut).append(record)
        currentFile.close()

'''
writeRootDir = "C:\\Users\\wbl\\Desktop\\ETC\\StationIn"
for key in stationInDict.keys():
    stationInDict.get(key).sort(key=lambda passRecord: passRecord.dateIn)
    writeFile = codecs.open(writeRootDir + '\\' + key + ".txt", 'w', 'utf-8')
    for record in stationInDict.get(key):
        line = record.dateIn + ',' + record.stationIn + ',' + record.dateOut + ',' + record.stationOut + ',' + \
               str(record.fee) + ',' + record.plateNum + ',' + record.vehicleType
        print line
        writeFile.write(line + '\n')
    writeFile.close()
'''


writeRootDir = "C:\\Users\\wbl\\Desktop\\ETC\\StationOut"
for key in stationOutDict.keys():
    stationOutDict.get(key).sort(key=lambda passRecord: passRecord.dateOut)
    writeFile = codecs.open(writeRootDir + '\\' + key + ".txt", 'w', 'utf-8')
    for record in stationOutDict.get(key):
        line = record.dateIn + ',' + record.stationIn + ',' + record.dateOut + ',' + record.stationOut + ',' + \
               str(record.fee) + ',' + record.plateNum + ',' + record.vehicleType
        print(line)
        writeFile.write(line + '\n')
    writeFile.close()
