import sys
import datetime

f=open("xxx")
i=0
f0=open(sys.argv[3][:-1]+"logCout","r")
f1=open(sys.argv[3][:-1]+"log","a")
f2=open("log","a")
f3=open("logCout","r")
for passwd in f:
    if i==int(sys.argv[2]):
        if sys.argv[1][0:4]==passwd[0:4]:
            print(1)
            f1.write(str(datetime.datetime.now())[0:16]+"/"+"введён верный mail код\n")
        else:
            print(0)
            f1.write(str(datetime.datetime.now())[0:16]+"/"+"введён неверный mail код\n")
            f2.write(str(datetime.datetime.now())[0:16]+"/участок "+sys.argv[3][:-1]+"/введён неверный mail код"+"\n")
            buffer=str(int(f3.read())+1)
            f3.close()
            f3=open("logCout","w+")
            f3.write(buffer)
        break
    else:
        i+=1
buffer=str(int(f0.read())+1) 
f0.close()
f0=open(sys.argv[3][:-1]+"logCout","w+")
f0.write(buffer)
f0.close()
f1.close()
f2.close()
f.close()
