#/bin/bash
for i in $(ls /home/); do
	#echo $i
  	echo "User: $i $(cd /home/$i; du -sh) /home/$i"
	echo ""
done

