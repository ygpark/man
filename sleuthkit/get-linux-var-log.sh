#!/bin/sh

# fls result is 
# 	r/r 7867795:     auth.log
#	r/r 7867795:     auth.log
#	r/r * 7800000(realloc): deleted/filename.log
#	r/r 7867795:     apache2/filename.log
		   
		   
for i in $(fls -F -r /dev/sdb1 7733451 | awk '(/[0-9]+:{print $2$3}' | grep -v "*")
do
	# The Format of $line is
	# 	00000:auth.log
	# 	00000:auth.log
	# 	00000:deleted_filename.log
	#   00000:apache2_filename.log
	
	line=$(echo $i | sed "s/\//_/g")   # change from '/' to '_'
	inod=$(echo $line | awk -F ':' '{print $1}')
	filename=$(echo $line | awk -F ':' '{print $2}')
	echo "Getting $filename........"
	icat /dev/sdb1 $inod > $filename
	
done