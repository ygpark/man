# -*- coding:utf-8 -*-
import glob

filelist = glob.glob("*.csv")

fw = open("one.csv", "wb")
print(len(filelist))
for filename in filelist:
    print(filename + "...working")
    fr = open(filename, "rb")
    text = fr.read()
    fw.write(text)
    fr.close()
    print(filename + "...done")
fw.close()
    
print("done")