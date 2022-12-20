from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import sys
import time
import pyotp
import qrcode
import sqlite3
import random




class Widget(Qt.QWidget):
	txt=[]
	def __init__(self,table):
		super().__init__()
		self.setWindowTitle("информация по кодам доступа пользователя с id "+sys.argv[1])
		timer = QtCore.QTimer(self, timeout=self.Cuff, interval=1000)
		timer.start()
		self.table = table
		layout = Qt.QVBoxLayout(self)
		sprbtn1=Qt.QPushButton("Показать qr-код для приложения с временными кодами")
		layout.addWidget(sprbtn1)
		sprbtn1.clicked.connect(self.bigger)
		sprbtn2=Qt.QPushButton("Выдать ПИН-код")
		layout.addWidget(sprbtn2)
		sprbtn2.clicked.connect(self.small)
		sprbtn=Qt.QPushButton("отметить все просмотренными")
		layout.addWidget(self.table)
		sprbtn.clicked.connect(self.Pomet)
		layout.addWidget(sprbtn)
		layout.addWidget(self.table)
		sprbtn.clicked.connect(self.Pomet)
		self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) 
		self.table.verticalHeader().setVisible(False)
		self.setMinimumSize(QSize(500, 700))
		self.show()

	def Cuff(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')
		cursor.execute("SELECT * FROM events WHERE UID=?",(sys.argv[1],))
		self.events=cursor.fetchall()
		connection.close()
		self.table.setRowCount(len(self.events))
		self.table.setColumnCount(2)
		self.table.setHorizontalHeaderLabels(["Время события","Тип события"])
		i=0
		for event in self.events:
			self.table.setItem(i, 0, QTableWidgetItem(event[1]))
			self.table.setItem(i, 1, QTableWidgetItem(event[2]))
			i += 1
		self.table.resizeColumnsToContents()

	def small(self):
		PIN=""
		for i in range(4):
			self.PIN=self.PIN+str(random.randrange(10))
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute("UPDATE Users SET PIN=? WHERE UID=?", (PIN,sys.argv[1]))
		os.system("python3 small.py "+str(sys.argv[1])+" "+PIN)
		connection.commit()
		connection.close()
	
	def bigger(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		key = pyotp.random_base32()
		cursor.execute("UPDATE Users SET key=? WHERE UID=?", (key,sys.argv[1]))
		connection.commit()
		cursor.execute("SELECT mail FROM Users WHERE UID=?", (sys.argv[1],))
		qrka=qrcode.make(pyotp.totp.TOTP(key).provisioning_uri(name=cursor.fetchall()[0][0], issuer_name='BiBeLock'))
		qrka.show()
		connection.close()


	def Pomet(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')
		cursor.execute("UPDATE events SET sost=? WHERE UID=?", ('0',sys.argv[1]))
		connection.commit()
		connection.close()


app = Qt.QApplication([])
w = Widget(Qt.QTableWidget())
sys.exit(app.exec_())

