import sys


f=open(sys.argv[1]+"log","w+")
f.close()
f=open(sys.argv[1]+"logCout","w+")
f.write('0')
f.close()
f=open(sys.argv[1]+"logCoutP","w+")
f.write('0')
f.close()
