import sys
from collections import defaultdict
import getIPWhois
import time
import json
start_time = time.time()

sampleData=sys.argv[1]

whiteList=defaultdict(set)

file_reader= open(sampleData)
read = file_reader.readlines()

SourceDestDict=defaultdict(set)
getIPWhoisLookUp=defaultdict()

#whiteList made from the iotOutgoindData

def initializingWhiteList(read):
    counter = 0
    for points in read:
        #print(counter)
        counter = counter + 1
        #print("--- %s seconds ---" % (time.time() - start_time))
        points = points.strip().split("\t")
        # print(points[0])
        sourceMAC = points[0]
        # print("sourceM= ",sourceMAC)
        destinationIP = str(points[5])
        # print("destio=",destinationIP)
        if destinationIP == None:
            continue

        SourceDestDict[sourceMAC]=SourceDestDict.get(sourceMAC,set())
        if destinationIP in SourceDestDict[sourceMAC]:
            continue
        SourceDestDict[sourceMAC].add(destinationIP)

        # if sourceMAC in SourceDestDict:
        #     if destinationIP in SourceDestDict[sourceMAC]:
        #         continue
        #     else:
        #         SourceDestDict[sourceMAC].add(destinationIP)
        # else:
        #     SourceDestDict[sourceMAC].add(destinationIP)


        if destinationIP in getIPWhoisLookUp:
            ipwhois_value=getIPWhoisLookUp.get(destinationIP)
        else:
            ipwhois_value = getIPWhois.getIPWhois(destinationIP)
            getIPWhoisLookUp[destinationIP]=(ipwhois_value)

        if ipwhois_value == None:
            continue
        name, description = ipwhois_value[0],ipwhois_value[1]

        print(name,destinationIP)

        if sourceMAC in whiteList:
            if destinationIP not in whiteList[sourceMAC]:
                whiteList[sourceMAC].add(name)
                whiteList[sourceMAC].add(description)
        else:
            whiteList[sourceMAC].add(name)
            whiteList[sourceMAC].add(description)

        print(whiteList)
initializingWhiteList(read)
final = {}
for x in whiteList:
	final[x] = list(whiteList[x])
json.dump(final, open('whiteList.json', 'w'))


