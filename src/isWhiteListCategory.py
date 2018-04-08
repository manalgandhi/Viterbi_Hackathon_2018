from collections import defaultdict
import os
import getWhiteList
import getIPWhois as gt

parent = os.path.abspath(os.path.join(".", os.pardir))
data = os.path.join(parent,"data")
entertainmentWhiteList=defaultdict(set)
homeWhiteList=defaultdict(set)
try:
    with open(os.path.join(data,"Devices.tsv"),encoding="utf-8") as f:
        for x in f.readlines()[1:]:
            y = x.split("\t")[0].strip()
            category= x.split("\t")[2].strip()
            mac = "".join([z.lower() for z in y if z.isalnum()])
            if category=='home_appliances':
                if mac in homeWhiteList.keys():
                    continue
                else:
                    entertainmentWhiteList[mac].add(z for z in getWhiteList.whiteList[mac])
            else:
                if mac in entertainmentWhiteList.keys():
                    continue
                else:
                    entertainmentWhiteList[mac].add(z for z in getWhiteList.whiteList[mac])
except:
    pass

def isWhitelistHomeAppliances(ip):
    for key in homeWhiteList.keys():
        if gt.getIPWhois(ip) in homeWhiteList[key]:
            return True
    return False

def isWhitelistEntertainment(ip):
    for key in entertainmentWhiteList.keys():
        if gt.getIPWhois(ip) in homeWhiteList[key]:
            return True
    return False

def isWhiteListDeviceCategory(category,ip):
    if category=='home_appliances':
        isWhitelistHomeAppliances(ip)
    elif category=='entertainment':
        isWhitelistEntertainment(ip)
    else:
        return True




