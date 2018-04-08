import os,json
import getIPWhois
import pickle
from collections import defaultdict


parent = os.path.abspath(os.path.join(".", os.pardir))
data = os.path.join(parent,"data")
whitelist = json.load(open(os.path.join(data,'whitelist.json'), 'r'))
generalWhiteList = json.load(open(os.path.join(data,'generalWhiteList.json'), 'r'))
def checkWhiteList(mac,ip):
	
	ipwhois_value=getIPWhois.getIPWhois(ip)
	
	mac = "".join([x.lower() for x in mac if x.isalnum()])
	if whitelist.get(mac,False):
		return ipwhois_value[0] in whitelist[mac] or ipwhois_value[1] in whitelist[mac]
	return False
		
def checkWhiteListIp(sip,ip):
	if generalWhiteList.get(sip,False):
		return ip in generalWhiteList[sip]
	return False

	
if __name__ == "__main__":
	print(checkWhiteListIp("147.32.83.53","147.32.80.105"))