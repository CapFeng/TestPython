# encoding=utf-8

from datetime import datetime

import matplotlib.pylab as plt
from pandas import Series, DataFrame
from statsmodels.tsa.arima_model import ARMA

timeSeriesPath = "C:\\Users\\wbl\\Desktop\\ETC\\totalIn\\鲁北.txt"
currentFile = open(timeSeriesPath, 'r', encoding='utf-8')

countDict = {}

for eachLine in currentFile:
    line = eachLine.strip()
    field = line.split(' ')
    time = field[0]
    number = field[1]
    countDict.setdefault(time, number)

currentFile.close()

items = countDict.items()
sorted(countDict.items())

count = []
date = []
day = []
hour = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
        '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

for i in range(401, 431):
    day.append(str(i).zfill(4))

frame = DataFrame(columns=hour, index=day)

# 先全部置空，再按照index赋值
for key, value in items:
    dateI = datetime.strptime(key, '%m%d%H')
    date.append('2016' + key + '0000')
    count.append(int(value))  # 因为从文件中直接读取，value会被默认为string，需要强制转换成int
    frame.ix[key[0:4], key[4:6]] = value

obj = Series(count, index=date)
objTest = obj.ix['2016040400':'2016041800']

# objTest.plot()  # 按照索引绘制两周的图表


# diff(T)函数，T为周期，也就是差分步数，而不是阶数，diff()函数本身就是做一阶差分的。
# 差分的index是当前值减去T周期之前的数据.
periodTest = objTest.diff(24)
# periodTest.plot()
# print(periodTest)

# 去除周期性之后再做一阶差分,得到平稳序列
diff1 = periodTest.diff(1)
# 差分之后去除之前的空值
inputDiff = diff1.ix['2016040501':'2016041800']

inputDiff.plot()
# plt.show()

model = ARMA(inputDiff, order=(3, 2))

resultARMA = model.fit(disp=-1, method='css', maxiter=60, trend='nc')    # 设置迭代次数为60，可以避免极大似然函数不收敛的问题

# nextValue = resultARMA.forecast(steps=1)[0]

# value = list(periodTest.tail(1).to_dict().values())
# print(value[0])
# periodTest.set_value(20160418000000, value[0] + nextValue)

# print(periodTest)
# print(objTest)
predictARMA = resultARMA.predict(start='20160406', end='20160430')
# print(predictARMA)

# print(objTest)
dateAdditon = Series(data=0, index=date).ix['2016041800':'2016042000']
objTest = objTest.append(dateAdditon)
periodTest = periodTest.append(dateAdditon)
diff1 = diff1.append(dateAdditon)

# 一阶差分还原,shift(1)向右移动1位
diffShift = periodTest.shift(1)

# print(periodTest)
# print(diffShift)

# print(periodTest.tail(1))
# print(diff1)
periodRecover = diffShift.add(predictARMA)
# periodRecover = diffShift.add(predictARMA)


# 周期性还原
periodShift = objTest.shift(24)
diff_recover = periodShift.add(periodRecover)
# diff_recover.plot()
diff_recover.dropna(inplace=True)

results = DataFrame(diff_recover)

# print(diff_recover.ix['20160406':'20160419'])
resultsAdd = diff_recover.ix['20160417':'20160418']
# print(diff_recover)

for i in range(0, 24):
    date = '20160418' + str(i).zfill(2) + '0000'
    objTest.set_value(label=date, value=round(resultsAdd[i]))

print(objTest)

periodTest1 = objTest.diff(24).ix['20160407':'20160425']
# print(periodTest)
diff2 = periodTest1.diff(1).ix['2016040701':'20160419']

model1 = ARMA(diff2, order=(3, 2))

resultARMA1 = model1.fit(disp=1, method='css', maxiter=60, trend='nc')    # 设置迭代次数为60，可以避免极大似然函数不收敛的问题

predictARMA1 = resultARMA1.predict(start='20160408', end='20160420')
print(predictARMA1)
diffShift1 = periodTest1.shift(1)

periodRecover1 = diffShift1.add(predictARMA1)


# print(objTest.ix['20160417':'20160420'])

periodShift1 = objTest.shift(24)
diff_recover1 = periodShift1.add(periodRecover1)
res = DataFrame(diff_recover1)
# print(diff_recover1.ix['20160407':'20160420'])
res.plot()
plt.show()

