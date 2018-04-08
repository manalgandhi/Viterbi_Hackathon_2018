from getIPWhois import getIPWhois
import codecs
import json
import time

result_data = {}
with codecs.open('/Users/ManalGandhi/Downloads/out.txt', 'r', 'utf-8') as infile:
    jj = json.load(infile)

    ipdata = jj['ipData']
    for prod in ipdata:
        print(prod)
        result_data[prod] = {}
        ip_processed = set()
        for ip in ipdata[prod]:
            if ip in ip_processed:
                continue
            ip_processed.add(ip)
            try:
                name = getIPWhois(ip)
            except:
                continue
            #time.sleep(1)
            if name is not None:
                result_data[prod][name[0]] = True

    count_dict = {}
    for prod in result_data:
        count_dict[prod] = len(result_data[prod])

print(count_dict)


