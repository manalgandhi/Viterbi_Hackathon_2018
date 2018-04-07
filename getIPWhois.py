from ipwhois import IPWhois

def getIPWhois(ip):
    obj=IPWhois(ip)
    result=obj.lookup_rws()
    return result['nets'][0]['name']


#print getIPWhois('74.125.227.206')