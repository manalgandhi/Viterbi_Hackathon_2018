import sys
import codecs, csv
from isBlackListed import isBlackList
import getMac
from getIPWhois import getIPWhois
from getDeviceType import get_device_type
import getWhiteList as getWhiteList
from isWhiteListCategory import isWhiteListDeviceCategory
from isWhiteListCategory import isWhitelistEntertainment
from isWhiteListCategory import isWhitelistHomeAppliances
from datetime import datetime

class process_input:
    def __init__(self, file_name):
        self.input_file = file_name
        self.hold_past_records = {}
        self.past_record_per_source = {}
        self.source_ip_category = {}
        self.contained_whitelist = {}

    def read_test_data(self, output_file):
        # Read test data
        with codecs.open(output_file, 'w', 'utf-8') as outfile:
            csvwriter = csv.writer(outfile)
            with codecs.open(self.input_file, 'r', 'utf-8') as infile:
                csvreader = csv.reader(infile)
                header_line = next(csvreader)
                self.header_dict = {}
                for i in range(0, len(header_line)):
                    self.header_dict[header_line[i]] = i
                count = 1
                print("Started processing input file")
                for line in csvreader:
                    count+=1
                    giveAccess, reason = self.process_data(line)
                    line.append(1 if giveAccess is False else 0)
                    line.append(reason)
                    csvwriter.writerow(line)
                    if count % 100 == 0:
                        print("Processed "+str(count)+" lines")
                    outfile.flush()


    # returns true if it is blocked
    def process_data(self, line):
        source_ip = line[self.header_dict['SIP']]
        source_mac = line[self.header_dict['SMAC']]
        source_port = line[self.header_dict['Sport']]
        dest_ip = line[self.header_dict['DIP']]
        dest_mac = line[self.header_dict['DMAC']]
        dest_port = line[self.header_dict['Dport']]
        protocol = line[self.header_dict['Protocol']]

        #print("Start evaluating: "+str(datetime.now()))
        if source_ip not in self.hold_past_records:
            self.hold_past_records[source_ip] = (set(), set())
            self.past_record_per_source[source_ip] = 0
        destination_name = getIPWhois(dest_ip)
        if destination_name is not None:
            destination_name = destination_name[0]
            self.hold_past_records[source_ip][0].add(destination_name)
        self.hold_past_records[source_ip][1].add(dest_ip)

        if protocol.upper() in ["MDNS", "EAPOL", "ARP", "DNS", "XID"]:
            return False, "Safe protocol"

        self.past_record_per_source[source_ip] = self.past_record_per_source[source_ip] + 1

        #check blacklist file
        #print("Check blacklist evaluating: " + str(datetime.now()))
        if isBlackList(source_ip, source_mac) or isBlackList(dest_ip, dest_mac):
            return True, "IP Blacklisted"

        #print("Check if known device evaluating: " + str(datetime.now()))
        #check if it is a known device
        device_info = getMac.getMacDetails(source_mac)
        if device_info is not None:
            if getWhiteList.checkWhiteList(source_mac, dest_ip):
                return False,"Source mac and Dest IP whitelisted"#dont block
            elif isWhiteListDeviceCategory(device_info['category'],dest_ip):
                return False, "Source device category and dest IP whitelisted"
        device_info = getMac.getMacDetails(dest_mac)
        if device_info is not None:
            if getWhiteList.checkWhiteList(dest_mac, source_ip):
                return False, "Dest mac and source ip whitelisted"#dont block
            elif isWhiteListDeviceCategory(device_info['category'],source_ip):
                return False, "Dest device and source ip whitelisted"

        if getWhiteList.checkWhiteListIp(source_ip, dest_ip):
            return False, "source ip and dest ip pair swhitelisted"

        #print("Unknown device evaluating: " + str(datetime.now()))
        #unknown device, categorize data
        if(self.past_record_per_source[source_ip] < 15):
            return False, "source ip is relatively new"#dont block
        elif source_ip not in self.source_ip_category:
            device_category = get_device_type(len(self.hold_past_records[source_ip][0]))
            self.source_ip_category[source_ip] = device_category
            dest_name_list = [l for l in self.hold_past_records[source_ip][0]]
            dest_ip_addr = [l for l in self.hold_past_records[source_ip][1]]
            self.contained_whitelist[source_ip] = (dest_name_list, dest_ip_addr)
        device_category = self.source_ip_category[source_ip]
        if device_category is "general_purpose":
            return False, "General category"
        elif device_category is "home_appliances" and isWhitelistHomeAppliances(dest_ip):
            return False, "Whitelisted home appliance"
        elif device_category is "entertainment" and isWhitelistEntertainment(dest_ip):
            return False, "Whitelisted entertainment"
        elif destination_name in self.contained_whitelist[source_ip][0] or dest_ip in self.contained_whitelist[source_ip][1]:
            return False, "Previously seen destination. Letting through."
        elif dest_ip in self.contained_whitelist and source_ip in self.contained_whitelist[dest_ip][1]:
            return False, "Previously seen source. Letting through."
        else:
            return True, "Default"


if __name__ == '__main__':
    file_name = sys.argv[1]
    output_file = sys.argv[2]
    p = process_input(file_name)
    p.read_test_data(output_file)