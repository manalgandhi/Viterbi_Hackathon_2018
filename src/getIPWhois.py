import ipwhois as ipw

def getIPWhois(ip):
    try:
        obj=ipw.IPWhois(ip)
        #raise ipw.ipwhois.WhoisLookupError
    # except ipw.ipwhois.IPDefinedError:
    #     return
    # except  ipw.ipwhois.WhoisLookupError:
    #     return
    # except ValueError:
    #     return 'ip_invalid'
        result = obj.lookup_rws()
        return result['nets'][0]['name'], result['nets'][0]['description']
    except:
        pass
    finally:
        return None


print getIPWhois('191.233.81.105')