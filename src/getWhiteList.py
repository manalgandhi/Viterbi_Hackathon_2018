import os,json
import getIPWhois
import pickle
from collections import defaultdict


parent = os.path.abspath(os.path.join(".", os.pardir))
data = os.path.join(parent,"data")
whitelist = json.load(open(os.path.join(data,'whitelist.json'), 'r'))
def checkWhiteList(mac,ip):
	
	ipwhois_value=getIPWhois.getIPWhois(ip)
	
	mac = "".join([x.lower() for x in mac if x.isalnum()])
	if whitelist.get(mac,False):
		return ipwhois_value[0] in whitelist[mac] or ipwhois_value[1] in whitelist[mac]
	else:
		return False

	
if __name__ == "__main__":
	print(checkWhiteList("94:10:3e:cd:37:65","64.210.203.208"))