import sys
import sqlite3
import pyotp


connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                    (UID TEXT, sname TEXT, name TEXT, mail TEXT, PIN TEXT, key TEXT)''')
UID=sys.argv[1][:sys.argv[1].index('|')]
print(UID)
cursor.execute("SELECT PIN FROM Users WHERE UID=?", (UID,))
ifrf=cursor.fetchall()[0][0]
if ifrf:
	cursor.execute("SELECT key FROM Users WHERE UID=?", (UID,))
	tapt=pyotp.TOTP(cursor.fetchall()[0][0])
	if sys.argv[1][sys.argv[1].index('|')+1:] == ifrf+tapt.now():
		print(1)
	else:
		print(0)
else:
	print(0)

