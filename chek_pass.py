import sys
import datetime

num=sys.argv[1][0:sys.argv[1].find("*")];
f=open(num)
cout=0
f0=open(num+"logCout","r")
f1=open(num+"log","a")
f2=open("log","a")
f3=open("logCout","r")

for passwd in f:
	if sys.argv[1][0:sys.argv[1].find("*")+5]==passwd[0:sys.argv[1].find("*")+5]:
		cout=1
		f1.write(str(datetime.datetime.now())[0:16]+"/введён верный основной код"+"\n")
		break
if cout == 0:
	f1.write(str(datetime.datetime.now())[0:16]+"/введён неверный основной код"+"\n")
	f2.write(str(datetime.datetime.now())[0:16]+"/участок "+num+"/введён неверный основной код"+"\n")
	buffer=str(int(f3.read())+1)
	f3.close()
	f3=open("logCout","w+")
	f3.write(buffer)
buffer=str(int(f0.read())+1) 
f0.close()
f0=open(num+"logCout","w+")
f0.write(buffer)
f0.close()
f.close()
f1.close()
f2.close()
f3.close()
print(cout)
