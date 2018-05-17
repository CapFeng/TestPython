# encoding=utf-8
from DataPreProcess.Function import *

file = "C:\\Users\\wbl\\Desktop\\ETC\\StationOut\\济南西.txt"
currentFile = open(file, 'r', encoding='utf-8')

stationMap = {}

for eachLine in currentFile:
    stationIn = eachLine.strip().split(',')[1]
    Function.insertRecords(stationIn, stationMap, 1)

stationItem = sorted(stationMap.items(), key=lambda k: k[1], reverse=True)

for item in stationItem:
    print(item[0] + '\t' + str(item[1]))
