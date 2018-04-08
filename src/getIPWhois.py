import ipwhois as ipw

def getIPWhois(ip):
    try:
        obj=ipw.IPWhois(ip)
    except ipw.ipwhois.IPDefinedError:
        return
    result=obj.lookup_rws()
    return result['nets'][0]['name'],result['nets'][0]['description']


#print getIPWhois('172.17.25.25')