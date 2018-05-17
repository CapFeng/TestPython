# encoding=utf-8
import matplotlib.pyplot as plt

file = "C:\\Users\\wbl\\Desktop\\ETC\\totalNewSHK\\机场.txt"

Hour = range(0, 24, 1)
currentFile = open(file, 'r')

recordMap = {}

text = currentFile.readlines()

while text:
    lines = text[:24]
    record = []
    date = lines[0].split('\t')[0][0:8]
    for line in lines:
        record.append(line.strip().split('\t')[1])
    recordMap.setdefault(date, record)
    text = text[24:]

currentFile.close()

fig = plt.figure()
ax = fig.gca()

for date, record in recordMap.items():
    plt.plot(Hour, record, label=date)

plt.title('JiChang')
plt.legend()
plt.show()
