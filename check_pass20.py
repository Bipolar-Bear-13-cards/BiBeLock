import sys
import sqlite3
import pyotp
import datetime


connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                    (UID TEXT, sname TEXT, name TEXT, mail TEXT, PIN TEXT, key TEXT)''')
UID=sys.argv[1][:sys.argv[1].index('|')]
cursor.execute("SELECT PIN FROM Users WHERE UID=?", (UID,))
ifrf=cursor.fetchall()
cursor1 = connection.cursor()
cursor1.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')


if ifrf:
	PIN=ifrf[0][0]
	cursor.execute("SELECT key FROM Users WHERE UID=?", (UID,))
	tapt=pyotp.TOTP(cursor.fetchall()[0][0])
	if sys.argv[1][sys.argv[1].index('|')+1:-1] == PIN+str(tapt.now()):
		print(1)
		tekevent=[(UID,str(datetime.datetime.now())[0:16],"введены верные учётные данные",'1')]
	else:
		print(0)
		tekevent=[(UID,str(datetime.datetime.now())[0:16],"введены неверные постоянный и/или временный коды",'1')]
else:
	print(0)
	tekevent=[(UID,str(datetime.datetime.now())[0:16],"считана отсутсвующая в базе данных метка",'1')]
cursor1.executemany("INSERT INTO events VALUES (?, ?, ?, ?)", tekevent)
connection.commit()
connection.close()



