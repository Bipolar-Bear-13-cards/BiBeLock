#!/bin/sh
stty -F /dev/ttyUSB0 cs8 9600 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts raw
	while read LINE
	do
	sudo python3 reg1.py $LINE
	exit
	done < /dev/ttyUSB0

