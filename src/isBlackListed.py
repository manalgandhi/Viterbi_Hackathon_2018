import os
import requests
from bs4 import BeautifulSoup

parent = os.path.abspath(os.path.join(".", os.pardir))
data = os.path.join(parent, "data")
ip_map = {}
with open(os.path.join(data, "blacklist_ip.tsv"), encoding="utf-8") as f:
    for x in f.readlines():
        row = x.split("\t")
        ip = row[0].strip()
        mac = "" if len(row) == 1 else row[1].strip()
        mac = [z.lower() for z in mac if z.isalnum()]
        mac = ''.join(mac)
        ip_map[ip] = mac

def isBlackList(c, mac):
    try:
        if ip in ip_map:
            mac = [z.lower() for z in mac if z.isalnum()]
            mac = ''.join(mac)
            ip_mac = ip_map[ip]
            if(len(ip_mac) < 1):
                return True
            if mac == ip_mac:
                return True
        #return False
        # #print("INSIDE ")
        r = requests.post('http://www.ipvoid.com/ip-blacklist-check/', data = {'ip': ip})
        #print r.text
        soup = BeautifulSoup(r.text,"html.parser")
        table = soup.find("table", attrs= {"class" : "table table-striped table-bordered"})

        if table != None:

                headings = [th.get_text() for th in table.find("tr").find_all("td")]

                datasets = []
                for row in table.find_all("tr")[1:]:
                    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
                    datasets.append(dataset)

                getIPSplit = str(datasets[0][1]).split(",")
                #print "This is the IP " + getIPSplit[1]

                if "BLACKLISTED" in getIPSplit[1]:
                        return True
                else:
                        return False
        else:
                #print "Invalid IP"
                return False
    except:
        return False


#print (isBlackList('216.58.216.14'))