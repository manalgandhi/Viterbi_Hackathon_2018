import codecs, csv
import sys


def get_decimal_ip(ip):
    try:
        blocks = ip.split('.')
        # 1.2.3.4 => 1*256^3 + 2*256^2 + 3*256^1 + 4*256*0
        decimal_ip = (int(blocks[0]) * 16777216) + (int(blocks[1]) * 65536) + (int(blocks[2]) * 256) + (int(blocks[3]))
        return decimal_ip
    except:
        return None


date = sys.argv[1]
filename = sys.argv[2]
data_type = sys.argv[3]
outfile = sys.argv[4]

out_row_list = []
out_row_list.append(
    ["Date", "Time", "Source MAC", "Source IP", "Source Port", "Dest MAC", "Dest IP", "Dest Port", "Protocol",
     "Good packet", "Allowed"])

with codecs.open(filename, 'r', 'utf-8') as infile:
    tsvreader = csv.reader(infile, delimiter="\t")

    header_row = next(tsvreader)
    header_dict = {}
    for i in range(0, len(header_row)):
        header_dict[header_row[i]] = i

    for row in tsvreader:
        try:
            protocol = row[header_dict.get('Proto')]
            time = row[header_dict.get('StartTime')]
            time = time[:time.rfind('.')]
            from_ip = row[header_dict.get('SrcAddr')]
            to_ip = row[header_dict.get('DstAddr')]

            if 'Sport' in header_dict and int(header_dict.get('Sport')) < len(row):
                from_port = row[header_dict.get('Sport')]
            else:
                from_port = ''
            if 'Dport' in header_dict and int(header_dict.get('Dport')) < len(row):
                to_port = row[header_dict.get('Dport')]
            else:
                to_port = ''

            if 'SrcMac' in header_dict and int(header_dict.get('SrcMac')) < len(row):
                from_mac = row[header_dict.get('SrcMac')]
            else:
                from_mac = ''
            if 'DstMac' in header_dict and int(header_dict.get('DstMac')) < len(row):
                to_mac = row[header_dict.get('DstMac')]
            else:
                to_mac = ''

            if get_decimal_ip(from_ip) == None and get_decimal_ip(to_ip) == None:
                continue

            out_row = []
            out_row.append(date)
            out_row.append(time)
            out_row.append(from_mac)
            out_row.append(from_ip)
            out_row.append(from_port)
            out_row.append(to_mac)
            out_row.append(to_ip)
            out_row.append(to_port)
            out_row.append(protocol)
            out_row.append('')
            out_row.append(data_type)
            out_row_list.append(out_row)
        except Exception as ex:
            print("Could not process row: " + str(row))
            print(ex)

with codecs.open(outfile, 'w', 'utf-8') as outfile:
    csvwriter = csv.writer(outfile)
    for row in out_row_list:
        csvwriter.writerow(row)