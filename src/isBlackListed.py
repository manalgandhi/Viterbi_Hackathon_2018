import requests
from getIPWhois import getIPWhois
from bs4 import BeautifulSoup


def isBlackList(d_IP):
    try:
        #print("INSIDE ")
        r = requests.post('http://www.ipvoid.com/ip-blacklist-check/', data = {'ip': d_IP})
        #print r.text
        soup = BeautifulSoup(r.text,"html.parser")
        table = soup.find("table", attrs= {"class" : "table table-striped table-bordered"})

        if table != None:
                headings = [th.get_text() for th in table.find("tr").find_all("td")]
                datasets = []
                for row in table.find_all("tr")[1:]:
                    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
                    #file.write(str(dataset))
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


#print isBlackList('192.168.100.65')