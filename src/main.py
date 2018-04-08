import sys
import codecs, csv
from isBlackListed import isBlackList
import getMac

class process_input:
    def __init__(self, file_name):
        self.input_file = file_name

    def read_test_data(self):
        # Read test data
        with codecs.open(self.input_file, 'r', 'utf-8') as infile:
            csvreader = csv.reader(infile)
            header_line = next(csvreader)
            self.header_dict = {}
            for i in range(0, len(header_line)):
                self.header_dict[header_line[i]] = i

            for line in csvreader:
                giveAccess = self.process_data(line)

    # returns true if it is blocked
    def process_data(self, line):
        source_ip = line[self.header_dict['Source IP']]
        source_mac = line[self.header_dict['Source MAC']]
        source_port = line[self.header_dict['Source Port']]
        dest_ip = line[self.header_dict['Dest IP']]
        dest_mac = line[self.header_dict['Dest MAC']]
        dest_port = line[self.header_dict['Dest Port']]
        protocol = line[self.header_dict['Protocol']]

        #check blacklist file
        if isBlackList(source_ip) or isBlackList(dest_ip):
            return True

        #check if it is a known device
        device_category = getMac.getMacDetails(source_mac)
        if device_category is None:
            device_category = getMac.getMacDetails(dest_mac)
        if device_category is not None:




        pass

    

if __name__ == '__main__':
    file_name = sys.argv[1]
    p = process_input(file_name)