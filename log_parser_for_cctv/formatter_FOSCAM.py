# -*- coding: utf-8 *-
import glob
import re

filelist = glob.glob("*.txt")
print("file count is " + str(len(filelist)))

for fname in filelist:
    print(fname + "...working")
    f1 = open(fname, "r")
    f2 = open(fname.split(".txt")[0]+".csv", "w")
    for line in f1.readlines():
        
        p_ip = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
        pattern = "(\w+, )(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})([ ]{3,}|\t)(.*)"
        #          \1     \2                                   \3        
        # Wed, 2017-08-16 14:42:39   admin          174.114.10.40     access
        # \1   \2                    \3        
        p_data = re.compile(pattern)
        
        if p_data.search(line) is not None and p_ip.search(line) is not None:
            cam_ip = fname.split(".txt")[0] # camera ip
            timestamp = re.sub(pattern, r"\2", line) #date
            log = re.sub(pattern, r"\4", line) #log
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
            
            newline = cam_ip + "," + timestamp + "," + external_ip + "," + log + "," + "FOSCAM" + "\n"
            
            #print(newline)
            f2.write(newline)
    f1.close()
    f2.close()
    print(fname + "...done")
            
            
            
