# encoding=utf-8


class Function:

    def __init__(self, pathString, provinceList=[]):
        self.pathString = pathString
        self.provinceList = provinceList

    def getProinvceList(self):
        return self.provinceList

    @staticmethod
    def judgeMonth(monthString):
        if int(monthString) in range(401, 431):
            return True
        else:
            return False

    def setProvinceList(self):
        stationFile = open(self.pathString, 'r')
        for eachLine in stationFile:
            stationName = eachLine.strip().split(',')[2]
            self.provinceList.append(stationName)

    def judgeStation(self,stationName):
        if stationName in self.getProinvceList():
            # print stationName + " is in This Province!"
            return True
        else:
            # print stationName + " is not in This Province!"
            return False
    @staticmethod
    def insertRecords(key, countDict, num):
        if key not in countDict.keys():
            countDict.setdefault(key, num)
        else:
            count = countDict.get(key) + num
            countDict[key] = count


    @staticmethod
    def getVehicleType(flagString):
        flag = int(flagString)
        tempDict = {
            1: '一',
            2: '二',
            3: '三',
            4: '四',
            5: '五',
            6: '六',
        }
        if flag in range(1, 7):
            vehicle = "客"
        elif flag in range(11, 17):
            vehicle = "货"
        else:
            vehicle = "未知"

        return vehicle + tempDict.get(flag % 10, '')



