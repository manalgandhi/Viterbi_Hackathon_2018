def isIp(string):
    return len(string.split("."))==4


input=open("dataset.csv")
bl=open("blackList.txt","w+")
bad=set()
good=set()
blackList=set()
for line in input:
    line=line.replace("\"","")
    split=line.split(",")
    label=split[13]
    src=split[0]
    dest=split[2]
    if (label==1):
        good.add(src)
        good.add(dest)
    else:
        bad.add(src)
        bad.add(dest)
for ip in bad:
    if ip not in good:
        bl.write(ip+"\n")