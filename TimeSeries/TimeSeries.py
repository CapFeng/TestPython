# encoding=utf-8

"""
本程序主要目的是对流量数据通过ARMA模型进行拟合和预测。具体的思路是，首先对数据进行DataFrame的处理（需要插入日期格式）；
其次是对DataFrame进行处理，比如，趋势分解，标准化，然后对残差部分进行ARMA模型训练；
ARMA模型训练的参数选取标准主要是aic、bic、hqic三种，选择数值最小aic对应的模型阶数p、q;
训练数据通过MLE等训练方法，得出相应的ARMA模型，以及对应的p阶和q阶权值；
然后通过调用 predict和forecast方法，对模型进行预测，预测结果很快收敛，说明我们的模型只能做短期预测。
"""

from datetime import datetime

import matplotlib.pylab as plt
import statsmodels.api as sm
from pandas import Series, DataFrame
from statsmodels.tsa.arima_model import ARMA

timeSeriesPath = "C:\\Users\\wbl\\Desktop\\Result\\totalIn\\鲁北.txt"
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
objTest = obj.ix['2016040400':'2016041823']
objTest.plot()  # 按照索引绘制两周的图表

# diff(T)函数，T为周期，也就是差分步数，而不是阶数，diff()函数本身就是做一阶差分的。
periodTest = objTest.diff(24)
# periodTest.plot()

# 去除周期性之后再做一阶差分,得到平稳序列
diff1 = periodTest.diff(1)
diff1.plot()

# 将数据的空值进行补全
diff1.dropna(inplace=True)

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(diff1, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(diff1, lags=40, ax=ax2)

# 由ACF和PACF图可以看出，参数可以暂且选择 p=3, q=2
# AIC, BIC, HQ信息量进行参数检验
# arma_mod70 = sm.tsa.ARMA(dta,(7,0)).fit()
# print(arma_mod70.aic,arma_mod70.bic,arma_mod70.hqic)
# arma_mod30 = sm.tsa.ARMA(dta,(0,1)).fit()
# print(arma_mod30.aic,arma_mod30.bic,arma_mod30.hqic)
# arma_mod71 = sm.tsa.ARMA(dta,(7,1)).fit()
# print(arma_mod71.aic,arma_mod71.bic,arma_mod71.hqic)
# arma_mod80 = sm.tsa.ARMA(dta,(8,0)).fit()
# print(arma_mod80.aic,arma_mod80.bic,arma_mod80.hqic)

# p=3, q=2的ARMA模型


model = ARMA(diff1, order=(3, 2))
resultArma = model.fit(disp=-1, method='css')

# 一阶差分还原
predictArma = resultArma.predict()
diffShift = periodTest.shift(1)
periodRecover = predictArma.add(diffShift)

# 周期性还原
periodShift = objTest.shift(24)
diff_recover = periodRecover.add(periodShift)

diff_recover.dropna(inplace=True)

# fig1 = plt.figure(figsize=(12, 8))
# ax1 = fig.add_subplot(211, diff_recover)
print(diff_recover)
# plt.subplots(diff_recover)
# diff_recover.plot()
# print(diff_recover.index)


# print(diff_recover.index + ' : ' + diff_recover.values)
plt.show()
