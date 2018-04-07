from ipwhois import IPWhois

def getIPWhois(ip):
    obj=IPWhois(ip)
    result=obj.lookup_rws()
    return result['nets'][0]['name'],result['nets'][0]['description']


##print getIPWhois('74.125.227.206')