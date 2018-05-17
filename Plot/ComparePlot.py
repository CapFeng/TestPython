import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mda

LR = [27.5, 41.9, 65.3, 76.5, 74.6, 69.9]
ARMA = [27.5, 44.2, 76.2, 67.6, 83, 77]
NN = [27.5, 63.6, 71.7, 74.6, 86.7, 70.8]
EM = [27.5, 56.4, 66.1, 73.5, 79.4, 67.0]
REAL = [9.0, 16.5, 27.5, 54.5, 58.5, 72.5, 83.0, 79.0]

X1 = ['2016042604', '2016042605']
X2 = ['2016042606', '2016042607', '2016042608', '2016042609', '2016042610', '2016042611']
X1.extend(X2)

start1 = datetime.datetime(2016, 4, 26, hour=4)
print(start1)
start2 = datetime.datetime(2016, 4, 26, hour=6)
end = datetime.datetime(2016, 4, 26, hour=11)
print(end)
delta = datetime.timedelta(hours=1)

date1 = mda.drange(start1, end, delta)
date2 = mda.drange(start2, end, delta)

ax = plt.gca()
# ax.plot_date(dates, Y, linestyle="-", marker=".")

ax.plot_date(date2, LR, linestyle="-", linewidth=2, marker='v', label='LR')
ax.plot_date(date2, ARMA, linestyle="-", linewidth=2, marker='.', label='ARMA')
ax.plot_date(date2, NN, linestyle="-", linewidth=2, marker='s', label='NN')
ax.plot_date(date2, EM, linestyle="-", color='blue', linewidth=2, marker='x', label='EM')
ax.plot_date(date1, REAL, linestyle="-", color='red', linewidth=2, marker='o', label='real')

plt.title('Different Algorithms in Prediction')
plt.legend()
plt.show()
