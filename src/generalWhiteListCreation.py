import sys
from collections import defaultdict
import json

generalWhiteList=defaultdict(set)
sampleData1=sys.argv[1]
sampleData2=sys.argv[2]

file_reader1= open(sampleData1)
read1 = file_reader1.readlines()[1:]

file_reader2=open(sampleData2)
read2=file_reader2.readlines()[1:]

for points in read1:
    points = points.strip().split(",")
    sourceIP = points[3]
    # print("sourceIP=", sourceIP)
    destIp = points[6]
    # print("DEST= ",destIp)

    if sourceIP in generalWhiteList:
        if destIp not in generalWhiteList[sourceIP]:
            generalWhiteList[sourceIP].add(destIp)
    else:
        generalWhiteList[sourceIP].add(destIp)

# print("**************************************************************************")
for points in read2:
    points = points.strip().split(",")
    sourceIP = points[3]
    # print("sourceIP=", sourceIP)
    destIp = points[6]
    # print("DEST= ",destIp)

    if sourceIP in generalWhiteList:
        if destIp not in generalWhiteList[sourceIP]:
            generalWhiteList[sourceIP].add(destIp)
    else:
        generalWhiteList[sourceIP].add(destIp)



print(generalWhiteList)
final = {}
for x in generalWhiteList:
	final[x] = list(generalWhiteList[x])
json.dump(final, open('generalWhiteList.json', 'w'))
