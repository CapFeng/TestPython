# encoding=utf-8


import os
import time

from DataPreProcess.Function import *

timeSeriesDirIn = "C:\\Users\\wbl\\Desktop\\ETC\\StationIn"
timeSeriesDirOut = "C:\\Users\\wbl\\Desktop\\ETC\\StationOut"


totalDirIn = "C:\\Users\\wbl\\Desktop\\ETC\\totalInNew"
#truckDirIn = "C:\\Users\\wbl\\Desktop\\ETC\\truckIn"
#carDirIn = "C:\\Users\\wbl\\Desktop\\ETC\\carIn"
totalDirOut = "C:\\Users\\wbl\\Desktop\\ETC\\totalOutNew"
#truckDirOut = "C:\\Users\\wbl\\Desktop\\ETC\\truckOut"
#carDirOut = "C:\\Users\\wbl\\Desktop\\ETC\\carOut"


totalDict = {}
TruckDict = {}
CarDict = {}


for fileName in os.listdir(timeSeriesDirIn):
    if not os.path.isdir(fileName):             #确认是文件
        totalDict = {}
        truckDict = {}
        carDict = {}
        currentFile = open(os.path.join(timeSeriesDirIn, fileName), 'r', encoding='utf-8')
        print(fileName)
        for eachLine in currentFile:
            line = eachLine.strip()
            field = line.split(',')
            if len(field) == 7:
                date = field[0][4:8]
                time = field[0][4:10]

            if Function.judgeMonth(date):               #确认是四月份的数据
                flag = field[6]
                if flag == '客一' or flag == '客二' or flag == '货一':
                    Function.insertRecords(time, totalDict, 1)
                    # Function.insertRecords(time, truckDict)
                elif flag == '客三' or flag == '客四' or flag == '货二':
                    Function.insertRecords(time, totalDict, 1.5)
                elif flag == '货三' or flag == '货四':
                    Function.insertRecords(time, totalDict, 2)
                elif flag == '货五':
                    Function.insertRecords(time, totalDict, 3)

        currentFile.close()
        sorted(totalDict.items())
        #sorted(truckDict.items())
        #sorted(carDict.items())

        totalFileIn = open(os.path.join(totalDirIn, fileName), 'w', encoding='utf-8')
        for key, value in totalDict.items():
            totalFileIn.write(str(key) + ' ' + str(value) + '\n')
        totalFileIn.close()
'''
        truckFileIn = open(os.path.join(truckDirIn, fileName), 'w', encoding='utf-8')
        for key, value in truckDict.items():
            truckFileIn.write(str(key) + ' ' + str(value) + '\n')
        truckFileIn.close()

        carFileIn = open(os.path.join(carDirIn, fileName), 'w', encoding='utf-8')
        for key, value in carDict.items():
            carFileIn.write(str(key) + ' ' + str(value) + '\n')
        carFileIn.close()
'''

for fileName in os.listdir(timeSeriesDirOut):
    if not os.path.isdir(fileName):             #确认是文件
        totalDict = {}
        truckDict = {}
        carDict = {}
        currentFile = open(os.path.join(timeSeriesDirOut, fileName), 'r', encoding='utf-8')
        print(fileName)
        for eachLine in currentFile:
            line = eachLine.strip()
            field = line.split(',')
            if len(field) == 7:
                date = field[0][4:8]
                time = field[0][4:10]

            if Function.judgeMonth(date):               #确认是四月份的数据
                flag = field[6]
                if flag == '客一' or flag == '客二' or flag == '货一':
                    Function.insertRecords(time, totalDict, 1)
                    # Function.insertRecords(time, truckDict)
                elif flag == '客三' or flag == '客四' or flag == '货二':
                    Function.insertRecords(time, totalDict, 1.5)
                elif flag == '货三' or flag == '货四':
                    Function.insertRecords(time, totalDict, 2)
                elif flag == '货五':
                    Function.insertRecords(time, totalDict, 3)
        currentFile.close()
        sorted(totalDict.items())
#        sorted(truckDict.items())
#        sorted(carDict.items())

        totalFileOut = open(os.path.join(totalDirOut, fileName), 'w', encoding='utf-8')
        for key, value in totalDict.items():
            totalFileOut.write(str(key) + ' ' + str(value) + '\n')
        totalFileOut.close()
'''
        truckFileOut = open(os.path.join(truckDirOut, fileName), 'w', encoding='utf-8')
        for key, value in truckDict.items():
            truckFileOut.write(str(key) + ' ' + str(value) + '\n')
        truckFileOut.close()

        carFileOut = open(os.path.join(carDirOut, fileName), 'w', encoding='utf-8')
        for key, value in carDict.items():
            carFileOut.write(str(key) + ' ' + str(value) + '\n')
        carFileOut.close()
'''

