# encoding=utf-8
import datetime

import matplotlib.dates as mda
import matplotlib.pyplot as plt

file = "C:\\Users\\wbl\\Desktop\\ETC\\totalNewSHK\\济南西.txt"

currentFile = open(file, 'r')
Y = []

recordMap = {}

for eachLine in currentFile:
    line = eachLine.strip()
    field = line.split('\t')
    date = field[0][0:8]
    rate = field[1]
    Y.append(rate)

currentFile.close()

start = datetime.datetime(2016, 4, 1)
end = datetime.datetime(2016, 5, 1)
delta = datetime.timedelta(hours=1)

dates = mda.drange(start, end, delta)

ax = plt.gca()
ax.plot_date(dates, Y, linestyle="-", marker=".")
plt.title('JiNanXi Total Traffic Flow')
plt.show()
