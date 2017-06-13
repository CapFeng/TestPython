# encoding=utf-8
class PassRecord:           # Python中不需要设置get和set...

    def __init__(self, stationIn, stationOut, dateIn, dateOut, fee, vehicleType, plateNum):
        self.stationIn = stationIn
        self.stationOut = stationOut
        self.dateIn = dateIn
        self.dateOut = dateOut
        self.fee = fee
        self.vehicleType = vehicleType
        self.plateNum = plateNum

    def __repr__(self):
        return repr((self.dateIn, self.stationIn, self.dateOut, self.stationOut,
                     self.fee, self.plateNum, self.vehicleType))




