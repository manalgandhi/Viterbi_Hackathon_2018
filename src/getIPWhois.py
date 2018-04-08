import ipwhois as ipw

gloabl_dict = {}
def getIPWhois(ip):
    if ip in gloabl_dict:
        return gloabl_dict[ip]
    try:
        obj=ipw.IPWhois(ip)
        result = obj.lookup_rws()
        data = (result['nets'][0]['name'], result['nets'][0]['description'])
        gloabl_dict[ip] = data
        return data
    except:
        gloabl_dict[ip] = None
        return None
    # finally:
    #     return None


if __name__ == "__main__":
	#print getIPWhois('104.16.66.50')
	pass