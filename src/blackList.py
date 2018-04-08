def isIp(string):
    return len(string.split("."))==4


input_bad=open('bad.csv')
input_good=open('good.csv')
bl=open("blackList.txt","w+")
bad=set()
good=set()
blackList=set()
ip2mac={}
for line in input_bad:
    line=line.replace("\"","")
    split=line.split(",")
    if len(split)>8:
        sip=split[2]
        dip=split[3]
        macs=split[7]
        macd=split[6]
        if isIp(sip):
            ip2mac[sip]=macs
            bad.add(sip)
        if isIp(dip):
            ip2mac[dip]=macd
            bad.add(dip)
for line in input_good:
    line=line.replace("\"","")
    split=line.split(",")
    
    if len(split)>8:
        sip=split[2]
        dip=split[3]
        if isIp(sip):
            good.add(sip)
        if isIp(dip):
            good.add(dip)  
for ip in bad:
    if ip not in good:
        bl.write(ip+"\t"+ip2mac[ip]+"\n")