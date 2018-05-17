# encoding=utf-8

import matplotlib.pylab as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm
from pandas import Series, DataFrame
from statsmodels.tsa.arima_model import ARMA

timeSeriesPath = "C:\\Users\\wbl\\Desktop\\ETC\\totalNewSHK\\济南西.txt"
currentFile = open(timeSeriesPath, 'r', encoding='utf-8')

Y = []
X = []
for eachLine in currentFile:
    field = eachLine.strip().split('\t')
    X.append(field[0])
    Y.append(float(field[1]))

dateIndex = pd.to_datetime(X, format='%Y%m%d%H')

# origin = pd.Series(Y, index=dateIndex)['2016-4-5':'2016-4-23']

origin = pd.Series(Y, index=dateIndex)

decompose = seasonal_decompose(origin, model='additive')

trend = decompose.trend
seasonal = decompose.seasonal
residual = decompose.resid

residual.dropna(inplace=True)
diff = residual.diff(1)
diff.dropna(inplace=True)

# ADF平稳性检验
check = adfuller(diff)

model = ARMA(diff, order=(5, 1))
result = model.fit(disp=-1, method='css')

predict = result.predict()

recover = predict.add(diff.shift(1))

final = recover.add(seasonal).add(trend)

# print(final['2016-04-29 08:00:00'])
# print(origin['2016-04-29 08:00:00'])

residual.plot(label='residual')
origin.plot(label='origin')
final.plot(label='predict')

plt.title('Compare: Predict and Origin')
plt.legend()
plt.show()

for item in final.items():
    print(item)
# print(final)
'''# Plot acf/pacf

fig = plt.figure()
ax1 = fig.add_subplot(211)
plot_acf(diff, ax=ax1)
ax2 = fig.add_subplot(212)
plot_pacf(diff, ax=ax2)

plt.show()
'''

'''# Plot trend/seasonal/residual

plt.subplot(411)
plt.plot(origin, label='origin')
plt.legend(loc='upper left')

plt.subplot(412)
plt.plot(trend, label='trend')
plt.legend(loc='upper left')

plt.subplot(413)
plt.plot(seasonal, label='seasonal')
plt.legend(loc='upper left')

plt.subplot(414)
plt.plot(residual, label='residual')
plt.legend(loc='upper left')

plt.show()
'''


