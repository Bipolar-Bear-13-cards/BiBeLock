import os
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import sys
import sqlite3
import pyotp
import qrcode
import random





class Widget(Qt.QWidget):
	pole1=[]
	pole2=[]
	pole3=[]
	def __init__(self,table):
		self.PIN=""
		for i in range(4):
			self.PIN=self.PIN+str(random.randrange(10))
		self.key = pyotp.random_base32()
		super().__init__()
		self.setWindowTitle("Добавление нового пользователя")
		layout1 = Qt.QVBoxLayout(self)
		txt1=Qt.QLabel("Фамилия:")
		self.pole1=Qt.QLineEdit()
		txt1.setAlignment(QtCore.Qt.AlignLeft)
		self.pole1.setAlignment(QtCore.Qt.AlignLeft) 
		txt2=Qt.QLabel("Имя:") 
		self.pole2=Qt.QLineEdit() 
		txt2.setAlignment(QtCore.Qt.AlignLeft) 
		self.pole2.setAlignment(QtCore.Qt.AlignLeft)
		txt3=Qt.QLabel("e-mail:") 
		self.pole3=Qt.QLineEdit() 
		txt3.setAlignment(QtCore.Qt.AlignLeft) 
		self.pole3.setAlignment(QtCore.Qt.AlignLeft)
		layout1.addWidget(txt1)
		layout1.addWidget(self.pole1)
		layout1.addWidget(txt2)
		layout1.addWidget(self.pole2)
		layout1.addWidget(txt3)
		layout1.addWidget(self.pole3)
		self.show()
		sprbtn1=Qt.QPushButton("Выдать ПИН-код")
		sprbtn1.clicked.connect(self.small)
		sprbtn2=Qt.QPushButton("Показать qr-код для приложения с временными кодами")
		sprbtn2.clicked.connect(self.bigger)
		sprbtn3=Qt.QPushButton("ОК")
		sprbtn3.clicked.connect(self.okk)
		sprbtn4=Qt.QPushButton("Отмена")
		sprbtn4.clicked.connect(self.cancel)
		layout1.addWidget(sprbtn1)
		layout1.addWidget(sprbtn2)
		layout1.addWidget(sprbtn3)
		layout1.addWidget(sprbtn4)

	def okk(self):
		#здесь должна быть запись пользователя в бд. ID находится в sys.argv[1]
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                    (UID TEXT, sname TEXT, name TEXT, mail TEXT, PIN TEXT, key TEXT)''')
		userid = [(sys.argv[1],self.pole1.text(),self.pole2.text(),self.pole3.text(),self.PIN,self.key)]
		cursor.executemany("INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?)", userid)
		connection.commit()
		connection.close()
		self.close()


	def cancel(self):
		self.close()

	def small(self):
		os.system("python3 small.py "+str(sys.argv[1])+" "+self.PIN)

	def bigger(self):
		qrka=qrcode.make(pyotp.totp.TOTP(self.key).provisioning_uri(name=self.pole3.text(), issuer_name='BiBeLock'))
		qrka.show()


f=open("test","w+")
f.write("ye")
f.close()
app1 = Qt.QApplication([])
w1 = Widget(Qt.QTableWidget())
f=open("test","w+")
f.write("no")
f.close()
sys.exit(app1.exec_())
