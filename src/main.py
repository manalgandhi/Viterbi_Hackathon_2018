import sys
import codecs, csv
from isBlackListed import isBlackList
import getMac
from getIPWhois import getIPWhois
from getDeviceType import get_device_type

class process_input:
    def __init__(self, file_name):
        self.input_file = file_name
        self.hold_past_records = {}
        self.past_record_per_source = {}
        self.source_ip_category = {}

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

                for line in csvreader:
                    giveAccess = self.process_data(line)
                    line.append(1 if giveAccess is False else 0)
                    csvwriter.write(line)

    # returns true if it is blocked
    def process_data(self, line):
        source_ip = line[self.header_dict['Source IP']]
        source_mac = line[self.header_dict['Source MAC']]
        source_port = line[self.header_dict['Source Port']]
        dest_ip = line[self.header_dict['Dest IP']]
        dest_mac = line[self.header_dict['Dest MAC']]
        dest_port = line[self.header_dict['Dest Port']]
        protocol = line[self.header_dict['Protocol']]

        if source_ip not in self.hold_past_records:
            self.hold_past_records[source_ip] = set()
            self.past_record_per_source[source_ip] = 0
        destination_name = getIPWhois(dest_ip)
        if destination_name is not None:
            self.hold_past_records[source_ip].add(destination_name)
        self.past_record_per_source[source_ip] = self.past_record_per_source[source_ip] + 1

        #check blacklist file
        if isBlackList(source_ip) or isBlackList(dest_ip):
            return True

        #check if it is a known device
        device_info = getMac.getMacDetails(source_mac)
        if device_info is not None:
            if isWhitelist(source_mac, dest_ip):
                return False#dont block
            elif isWhiteListDeviceCategory(device_info['category'], dest_ip):
                return False
        device_info = getMac.getMacDetails(dest_mac)
        if device_info is not None:
            if isWhitelist(dest_mac, source_ip):
                return False#dont block
            elif isWhiteListDeviceCategory(device_info['category'], source_ip):
                return False

        if isWhiteListNormal(source_ip, dest_ip):
            return False

        #unknown device, categorize data
        if(self.past_record_per_source[source_ip] < 30):
            return False#dont block
        elif source_ip not in self.source_ip_categorys:
            device_category = get_device_type(len(self.hold_past_records[source_ip]))
            self.source_ip_category[source_ip] = device_category
        device_category = self.source_ip_category[source_ip]
        if device_category is "general_purpose":
            return False
        elif device_category is "home_appliances" and isWhitelistHomeAppliances(source_ip, dest_ip):
            return False
        elif device_category is "entertainment" and isWhitelistEntertainment(source_ip, dest_ip):
            return False
        else:
            return True


if __name__ == '__main__':
    file_name = sys.argv[1]
    output_file = sys.argv[2]
    p = process_input(file_name)
    p.read_test_data(output_file)s