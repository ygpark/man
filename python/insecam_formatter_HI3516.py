# -*- coding: utf-8 *-
import glob
import re

filelist = glob.glob("*.txt")

for fname in filelist:
    f1 = open(fname, "r")
    f2 = open(fname.split(".txt")[0]+".csv", "w")
    for line in f1.readlines():
        #print(line)
        p_ip = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
        
        if ("로그 인" in line or "로그인" in line) and p_ip.search(line) is not None:
            
            # 0051    2016-12-24 19:56:03    로그 인            admin<Web:223.38.10.170>
            # \1      \2                     \3
            
            cam_ip = fname.split(".txt")[0] # camera ip
            timestamp = re.sub("(\d+)([ ]{3,}|\t)(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})([ ]{3,}|\t)(.*)", r"\3", line) #date
            log =       re.sub("(\d+)([ ]{3,}|\t)(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})([ ]{3,}|\t)(.*)", r"\5", line) #log
            external_ip = p_ip.search(log)[0]
            
            # 특수문자 정리           
            cam_ip = cam_ip.strip(' \r\n')
            timestamp = timestamp.strip(' \r\n')
            log = log.strip(' \r\n')
            log = log.replace(',','_')
            #print("cam_ip: " + cam_ip)
            #print("timestamp: " + timestamp)
            #print("log: " + log)
            #print("external_ip: " + external_ip)
            
            newline = cam_ip + "," + timestamp + "," + external_ip + "," + log + "," + "HI3516" + "\n"
            
            #print(newline)
            f2.write(newline)
    f1.close()
    f2.close()
            
            
            
            
