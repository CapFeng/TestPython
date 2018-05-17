# encoding=utf-8

import os
import time

from DataPreProcess.Function import *

timeSeriesDirIn = "C:\\Users\\wbl\\Desktop\\ETC\\StationIn"
timeSeriesDirOut = "C:\\Users\\wbl\\Desktop\\ETC\\StationOut"

totalDir = "C:\\Users\\wbl\\Desktop\\ETC\\totalNew"


for fileName in os.listdir(timeSeriesDirIn):
    if not os.path.isdir(fileName):             # 确认是文件
        totalDict = {}
        currentFileIn = open(os.path.join(timeSeriesDirIn, fileName), 'r', encoding='utf-8')

        print(fileName)
        for eachLine in currentFileIn:
            line = eachLine.strip()
            field = line.split(',')
            if len(field) == 7:
                date = field[0][4:8]
                time = (field[0][4:10])

            if Function.judgeMonth(date):               # 确认是四月份的数据
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

        currentFileIn.close()

        currentFileOut = open(os.path.join(timeSeriesDirOut, fileName), 'r', encoding='utf-8')
        for eachLine in currentFileOut:
            line = eachLine.strip()
            field = line.split(',')
            if len(field) == 7:
                date = field[0][4:8]
                time = (field[0][4:10])

            if Function.judgeMonth(date):               # 确认是四月份的数据
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
        currentFileOut.close()

        keyList = sorted(totalDict.keys())

        totalFile = open(os.path.join(totalDir, fileName), 'w', encoding='utf-8')
        for key in keyList:
            totalFile.write(str(key) + ' ' + str(totalDict[key]) + '\n')
        totalFile.close()
