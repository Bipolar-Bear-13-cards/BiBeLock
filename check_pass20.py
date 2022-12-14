import sys
import sqlite3
import pyotp
import datetime


#f=open("potom udalu.txt","w+")
#f.write ("я запущен\n")
connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                    (UID TEXT, sname TEXT, name TEXT, mail TEXT, PIN TEXT, key TEXT)''')
UID=sys.argv[1][:sys.argv[1].index('|')]
#f.write(UID+"\n")
cursor.execute("SELECT PIN FROM Users WHERE UID=?", (UID,))
#f.write(ifrf+"\n")
ifrf=cursor.fetchall()
cursor1 = connection.cursor()
cursor1.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT)''')




if ifrf:
	PIN=ifrf[0][0]
	cursor.execute("SELECT key FROM Users WHERE UID=?", (UID,))
	tapt=pyotp.TOTP(cursor.fetchall()[0][0])
	#f.write(str(len(sys.argv[1][sys.argv[1].index('|')+1:]))+"\n")
	#f.write(str(len(ifrf+str(tapt.now())))+"\n")
	#f.write(sys.argv[1][sys.argv[1].index('|')+1:]+"\n")
	#f.write(ifrf+str(tapt.now())+"\n")
	if sys.argv[1][sys.argv[1].index('|')+1:-1] == PIN+str(tapt.now()):
		#f.write("совпалдение!!!")
		print(1)
		tekevent=[(UID,str(datetime.datetime.now())[0:16],"введены верные учётные данные")]
	else:
		print(0)
		tekevent=[(UID,str(datetime.datetime.now())[0:16],"введены неверные постоянный и/или временный коды")]
else:
	print(0)
	tekevent=[(UID,str(datetime.datetime.now())[0:16],"считана отсутсвующая в базе данных метка")]
#f.close()
cursor1.executemany("INSERT INTO Users VALUES (?, ?, ?)", tekevent)
connection.close()



