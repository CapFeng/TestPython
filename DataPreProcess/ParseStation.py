# coding=utf-8


readFileName = "C:\\Users\\wbl\\Desktop\\ETC\\所有收费站.csv"

writeFile = open("C:\\Users\\wbl\\Desktop\\ETC\\shandongStationInfo.txt", 'w')

readFile = open(readFileName.decode('utf-8'), 'r')


for line in readFile:
    if "山东省" in line:
        print(line)
        writeFile.write(line)

readFile.close()
writeFile.close()
