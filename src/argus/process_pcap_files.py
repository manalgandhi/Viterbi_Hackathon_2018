from os import listdir
from os.path import isfile, join
import subprocess


argus_location = "/Users/ManalGandhi/Downloads/argus-3.0.8.2/bin/argus"
argus_client_location = "/Users/ManalGandhi/Downloads/argus-clients-3.0.8.2/bin/ra"

dir_path = "/Users/ManalGandhi/Downloads/Normal_Packets/"

pcap_files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

for file in pcap_files:
    print("Processing "+file)
    subprocess.call([argus_location, "-r", dir_path+file, "-w", dir_path+file+".argus"])
    print("Argus processing complete")
    subprocess.call(argus_client_location+" -n -c '\t' -r "+dir_path + file+".argus" +"-w " +dir_path + file + "_output_client -s stime saddr daddr proto sport dport smac dmac", shell=True)
    print("Argus client complete")
    subprocess.call(["python3", "/Users/ManalGandhi/PycharmProjects/Hackathon_USC_2018/src/process_argsoutput_file.py",
                     file[:10], dir_path + file + "_output_client", "1", dir_path + file + "_output.csv"])
    print("File converted")

