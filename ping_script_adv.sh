#!/bin/bash

echo "====================================="

if [ "$1" == " " ]
	then
		echo "You have to insert an IP address!"
		echo "Syntax:./ping_script_adv.sh 192.168.0"

else
	for ip in $(seq 1 254); do

	ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"  >> ip_list_nmap.txt & 
	done

cat ip_list_nmap.txt

echo "Will now start Nmap Scan for the finded IP address"
echo "====================================="

for ip in $(cat ip_list_nmap.txt); do nmap -sS -p 80 -T4 $ip & 

done
fi
