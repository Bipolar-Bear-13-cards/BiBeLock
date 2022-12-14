
#!/bin/sh

while [ true ]
do

stty -F /dev/ttyACM0 cs8 9600 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts raw
cout=0
sost=1
	while read LINE
	do
	if [ "$sost" -eq 0 ] && [ "$(expr $cout % 3)" -eq 0 ]; then
		np=$(python3 rand_pass.py $LINE)
		num=$LINE
		sost=1
	else
		if [ "$cout" -lt 3 ]; then
			res=$(python3 chek_pass.py $LINE)
			echo -n $res > /dev/ttyACM0
			if [ "$res" -eq 0 ]; then
				let "cout += 1"
				if [ "$cout" -eq 3 ]; then
					sost=0
				fi
			else
				cout=0
			fi
		else
			res=$(python3 exytro_chek_pass.py $LINE $np $num)
			echo -n $res > /dev/ttyACM0
			if [ "$res" -eq 0 ]; then
                        	let "cout += 1"
				if [ "$(expr $cout % 3)" -eq 0 ]; then
                                       	sost=0
                fi
			else
				cout=0
            fi
	   	fi
	fi
	done < /dev/ttyACM0
done
