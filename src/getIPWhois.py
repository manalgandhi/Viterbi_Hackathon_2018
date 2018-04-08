import ipwhois as ipw

def getIPWhois(ip):
    try:
        obj=ipw.IPWhois(ip)
    except ipw.ipwhois.IPDefinedError,ipw.ipwhois.WhoisLookupError:
        return
    except ValueError:
        return 'ip_invalid'
    result=obj.lookup_rws()
    return result['nets'][0]['name'],result['nets'][0]['description']


#print getIPWhois('1325.14.25.14')