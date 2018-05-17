import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mda
import numpy as np
from sklearn import linear_model
arma = []
nn = []
real = []

realName = "C:\\Users\\wbl\\Desktop\\KDDCup\\real.txt"
armaName = "C:\\Users\\wbl\\Desktop\\KDDCup\\ARMAPredict.txt"
nnName = "C:\\Users\\wbl\\Desktop\\KDDCup\\NNPredict.txt"

realfile = open(realName, 'r')
armafile = open(armaName, 'r')
nnfile = open(nnName, 'r')

for eachline in realfile:
    real.append(float(eachline.strip()))
realfile.close()

for eachline in armafile:
    arma.append(float(eachline.strip()))
armafile.close()

for eachline in nnfile:
    nn.append(float(eachline.strip()))
nnfile.close()


X = np.vstack((arma, nn)).T
# print(X)
Y = np.array([real]).T

# print(X)

reg = linear_model.LinearRegression()
reg.fit(X, Y)

predict = reg.predict(X)




'''
start = datetime.datetime(2016, 4, 25)
end = datetime.datetime(2016, 4, 30)
delta = datetime.timedelta(hours=1)
date = mda.drange(start, end, delta)

ax = plt.gca()
# ax.plot_date(dates, Y, linestyle="-", marker=".")

ax.plot_date(date, real, linestyle="-", linewidth=2, marker='v', label='REAL')
ax.plot_date(date, arma, linestyle="-", linewidth=2, marker='.', label='ARMA')
ax.plot_date(date, nn, linestyle="-", linewidth=2, marker='s', label='NN')
ax.plot_date(date, predict, linestyle="-", linewidth=2, marker='o', label='EM')

plt.title('Different Algorithms in Prediction')
plt.legend(loc=2)
plt.show()
'''


def mse(predict, observe, length):
    result = 0.0
    for i in range(length):
        result += np.square(predict[i]-observe[i])
    return result/length


def mae(predict, obesrve, length):
    result = 0.0
    for i in range(length):
        result += abs(predict[i]-obesrve[i])
    return result/length


def mape(predict, obesrve, length):
    result = 0.0
    count = 0
    for i in range(length):
        if obesrve[i] != 0 and obesrve[i] > 10:
            result += abs((predict[i]-obesrve[i])/(obesrve[i]))*100
            count += 1
    return result/count

# print(real[0:24])

mseTotal = mse(predict[96:120], real[96:120], 24)
maseTotal = np.sqrt(mseTotal)
maeTotal = mae(predict[96:120], real[96:120], 24)
mapeTotal = mape(predict[96:120], real[96:120], 24)
print(mseTotal)
print(maseTotal)
print(maeTotal)
print(mapeTotal)
