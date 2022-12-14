#!/bin/sh
while [ true ]
do
stty -F /dev/ttyACM0 cs8 9600 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts raw
        while read LINE
        do
        res=$(sudo python3 check_pass20.py $LINE)
	if [ true ]; then
		echo -n $res > /dev/ttyACM0
	fi
        done < /dev/ttyACM0
done
