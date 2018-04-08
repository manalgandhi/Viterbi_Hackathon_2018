import os

parent = os.path.abspath(os.path.join(".", os.pardir))
data = os.path.join(parent,"data")
def getMacDetails(mac):
    try:
        with open(os.path.join(data,"Devices.tsv"),encoding="utf-8") as f:
            for x in f.readlines():
                y = x.split("\t")
                mac = [z.lower() for z in mac if z.isalnum()]
                mac = ''.join(mac)
                eth = [z.lower() for z in y[0] if z.isalnum()]
                eth = ''.join(eth)

                if eth==mac:
                    return {"device":y[3],"category":y[2]}
        return None
    except:
        return None

def getMacVendor(mac):
    try:
        with open(os.path.join(data,"mac-vendor.txt"),encoding="utf-8") as f:
            for x in f.readlines():
                y = x.split("\t")
                mac = [z for z in mac if z.isalnum()][:6]
                eth = [z for z in y[0] if z.isalnum()]
                if eth==mac:
                    return y[1]
        return None
    except:
        return None

if __name__ == "__main__":
    print(getMacDetails("84:18:26:7b:5f:6b"))
    print(getMacVendor("84:18:26"))