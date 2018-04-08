import sys

class process_input:
	
	def __init__(self,file_name): 
		self.global_blacklist_of_ips = {}
		self.input_file = file_name

	def read_blacklist_file(self):
	#Read the global blacklist file of ips
		with open("/home/aish217/MS/PProjects/Graduate Hackathon/Viterbi_Hackathon_2018/data/blacklist_ip.tsv") as fp:  
   			line = fp.readline()
   			cnt = 1
   			while line:
   				key =line.split("\t")[0]
   				value = line.split("\t")[1].strip("\n")
   				self.global_blacklist_of_ips[key] = value
   				#print("Line {}: {}".format(cnt, line.strip()))
   				line = fp.readline()
   				cnt += 1

		return self.global_blacklist_of_ips

	
	def read_test_data():
	#Read test data
		with open("/home/aish217/MS/PProjects/Graduate Hackathon/Viterbi_Hackathon_2018/data/"+self.input_file) as fp:  
   			line = fp.readline()
   			cnt = 1
   			while line:
   				#self.global_blacklist_of_ips[key] = value
   				#print("Line {}: {}".format(cnt, line.strip()))
   				line = fp.readline()
   				cnt += 1
		#source and destination data of a packet	
		#src_ip = "192.168.0.1"
		#dest_ip = "192.168.0.2"

	def process_data():
	#Output blocked or not 
		pass
	#allowed_bit = 1;

	

	#if (src_ip in self.global_blacklist_of_ips) or (dest_ip in self.global_blacklist_of_ips):
		#allowed_bit = 0;
		#print("Not allowed");
	#else:
		#Determine src device info and destn device info
		#device_info_src = getDeviceinfo(src);
		#device_info_dest = getDeviceinfo(dest);

		#if(device_info_src != None):
			#Apply rules for that device type 
		#else:
			#Determine the brand of the device and apply rules
		
		#allowed_bit = 1;

if __name__ == '__main__':
	file_name = sys.argv[1]
	p = process_input(file_name)
	ip_list = p.read_blacklist_file()
	print(ip_list)