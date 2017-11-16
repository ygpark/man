import os

filenames = os.listdir(".")

for filename in filenames:
	if ".pcap" in filename:
		os.system("tshark -r " + filename + "  -Y \"pptp\"")