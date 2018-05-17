# encoding=utf-8

import matplotlib.pylab as plt
from pandas import Series, DataFrame
from statsmodels.tsa.arima_model import ARMA

timeSeriesPath = "C:\\Users\\wbl\\Desktop\\ETC\\totalIn\\鲁北.txt"
currentFile = open(timeSeriesPath, 'r', encoding='utf-8')

countDict = {}

# 从文件中读取日期和序列数据
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

# 先全部置空，再按照index赋值
for key, value in items:
    count.append(int(value))  # 因为从文件中直接读取，value会被默认为string，需要强制转换成int

origin = Series(count)
# objTest = obj.ix['2016040100':'2016043000']

# origin.plot()  # 按照索引绘制两周的图表


# diff(T)函数，T为周期，也就是差分步数，而不是阶数，diff()函数本身就是做一阶差分的。
period = origin.diff(24)
# period.plot()


# 去除周期性之后再做一阶差分,得到平稳序列
diff1 = period.diff(1)
# 差分之后去除之前的空值
inputDiff = diff1.dropna()
inputDiff.plot()
plt.show()

model = ARMA(count, order=(3, 2), dates='20160401000000', freq='B')

resultARMA = model.fit(disp=1, method='css', maxiter=60, trend='nc')    # 设置迭代次数为60，可以避免极大似然函数不收敛的问题

# print(resultARMA.)
# 模型预测
nextValue = resultARMA.forecast()[0]
print(nextValue)

# predictARMA = resultARMA.predict(start='20160406', end='20160430')
# print(predictARMA)

# 一阶差分还原
diffShift = periodTest.shift(1)


print(periodTest.tail(1))
# print(diff1)
# periodRecover = predictARMA.add(diffShift)
# periodRecover = diffShift.add(predictARMA)


# 周期性还原
periodShift = objTest.shift(24)
diff_recover = periodRecover.add(periodShift)

# diff_recover.dropna(inplace=True)
results = DataFrame(diff_recover)

# print(results)

results.plot()
# plt.show()
