from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import Qt, QtWidgets, QtCore
from PyQt5.QtCore import QSize
import sys
import time
import os
import random
import sqlite3





class Widget(Qt.QWidget):
	cout=[]
	table=[]
	sprbtn=[]
	sqr=[]
	btn3=[]
	btn4=[]
	btn5=[]
	btn6=[]
	btn7=[]
	def __init__(self,table):
		super().__init__()
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                    (UID TEXT, sname TEXT, name TEXT, mail TEXT, PIN TEXT, key TEXT)''')
		cursor.execute("SELECT * FROM Users")
		self.allusr=cursor.fetchall()
		connection.close()
		#self.n=n
		self.setWindowTitle("панель управления устройством контроля доступа")
		self.sprbtn=Qt.QPushButton()
		timer = QtCore.QTimer(self, timeout=self.Cuff, interval=5000)
		timer.start()
		self.table = table
		layout = Qt.QVBoxLayout(self)		
		self.table.setRowCount(len(self.allusr))
		self.table.setColumnCount(7)
		self.table.setHorizontalHeaderLabels(["","UID", "Фамилия","Имя", "E-mail","Количество новых сообщений о событиях"," "])
		i=0;
		for oneusr in self.allusr:
			self.sqr.append(Qt.QCheckBox())
			self.table.setCellWidget(i,0,self.sqr[i])
			self.btn3.append(Qt.QPushButton("подробнее"))
			self.table.setCellWidget(i, 6, self.btn3[i])
			self.btn3[i].clicked.connect(self.showLogOne)
			self.table.setItem(i, 1, QTableWidgetItem(oneusr[0]))
			self.table.setItem(i, 2, QTableWidgetItem(oneusr[1]))
			self.table.setItem(i, 3, QTableWidgetItem(oneusr[2]))
			self.table.setItem(i, 4, QTableWidgetItem(oneusr[3]))
			i+=1
			#self.btn4.append(Qt.QPushButton("удалить все сообщения о событиях"))
			#self.btn4[i].clicked.connect(self.deleteAllOne)
			#self.table.setCellWidget(i, 5, self.btn4[i])
			#self.btn5.append(Qt.QPushButton("сгенерировать новые коды входа"))
			#self.btn5[i].clicked.connect(self.NewCode)
			#self.table.setCellWidget(i, 6, self.btn5[i])
			#self.btn6.append(Qt.QPushButton("выдать код входа"))
			#self.btn6[i].clicked.connect(self.small)
			#self.table.setCellWidget(i, 7, self.btn6[i])
			#self.btn7.append(Qt.QPushButton("Сменить данные владельца"))
			#self.btn7[i].clicked.connect(self.changee)
			#self.table.setCellWidget(i, 8, self.btn7[i])
		layout.setAlignment(QtCore.Qt.AlignCenter)
		layout.addWidget(self.sprbtn)
		self.sprbtn.clicked.connect(self.showLog)
		sprbtn1=Qt.QPushButton("очистить историю попыток входа")
		sprbtn1.clicked.connect(self.deleteAll)
		layout.addWidget(sprbtn1)
		sprbtn2=Qt.QPushButton("выделить все")
		sprbtn2.clicked.connect(self.selectAll)
		layout.addWidget(sprbtn2)
		sprbtn3=Qt.QPushButton("удалить выбранных пользователей")
		sprbtn3.clicked.connect(self.del_usr)
		layout.addWidget(sprbtn3)
		sprbtn4=Qt.QPushButton("добавить пользователя")
		sprbtn4.clicked.connect(self.add_usr)
		layout.addWidget(sprbtn4)
		layout.addWidget(self.table)
		self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) 
		self.table.verticalHeader().setVisible(False)
		self.setMinimumSize(QSize(850, 700))
		#self.showMaximized()
		self.show()
		self.Cuff()

	def deleteAll(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')
		cursor.execute("DROP TABLE events")
		connection.commit()
		connection.close()



	def selectAll(self):
		for i in range(len(self.allusr)):
			self.sqr[i].setChecked(True)

	def del_usr(self):
		1

	def add_usr(self):
		os.system("(sudo python3 reg0.py &);sudo ./reg1.sh")
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM Users")
		self.allusr=cursor.fetchall()
		rowc=self.table.rowCount()
		self.table.insertRow(rowc)
		self.table.setItem(rowc, 1, QTableWidgetItem(self.allusr[-1][0]))
		self.table.setItem(rowc, 2, QTableWidgetItem(self.allusr[-1][1]))
		self.table.setItem(rowc, 3, QTableWidgetItem(self.allusr[-1][2]))
		self.table.setItem(rowc, 4, QTableWidgetItem(self.allusr[-1][3]))
		self.sqr.append(Qt.QCheckBox())
		self.table.setCellWidget(rowc,0,self.sqr[rowc])
		self.btn3.append(Qt.QPushButton("подробнее"))
		self.table.setCellWidget(rowc, 6, self.btn3[rowc])
		self.btn3[rowc].clicked.connect(self.showLogOne)

		

		

	def deleteAllOne(self):
		cout=999
		sender = self.sender()
		for i in range(self.n):
			if sender==self.btn4[i]:
				cout=i+1
				break
		os.system("python3 deleteAllOne.py "+str(cout))

	def showLogOne(self):
		cout=999
		sender = self.sender()
		for i in range(len(self.allusr)):
			if sender==self.btn3[i]:
				cout=i+1
				break
		os.system("python3 showLogOne.py "+self.allusr[cout][0])

	def showLog(self):
		os.system("python3 showLog.py")

	def NewCode(self):
		cout=999
		sender = self.sender()
		for i in range(self.n):
			if sender==self.btn5[i]:
				cout=i+1
				break
		f=open(str(cout),"w+")
		keys="1234567890ABCD"
		for j in range(6):
			passwd=""
			for k in range(4):
				passwd=passwd+keys[random.randint(0,13)]
			f.write(str(cout)+"*"+passwd+"\n")
		f.close()

	

	def Cuff(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		sum=0
		cursor.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')
		cursor.execute("SELECT COUNT(*) FROM events WHERE event=? AND sost=?", ("считана отсутсвующая в базе данных метка",'1'))
		sum += (cursor.fetchall()[0][0])
		cursor.execute("SELECT COUNT(*) FROM events WHERE event=? AND sost=?", ("введены неверные постоянный и/или временный коды",'1'))
		sum += (cursor.fetchall()[0][0])
		self.sprbtn.setText(str(sum)+" новых неудачных попыток(-ки) входа")
		#f.close()
		i=0
		for oneusr in self.allusr:
			#f=open(str(i)+"logCout")
			cursor.execute("SELECT COUNT(*) FROM events WHERE UID=? AND sost=?", (oneusr[0],'1'))
			self.table.setItem(i, 5, QTableWidgetItem(str(cursor.fetchall()[0][0])))
			i += 1
			#f.close()
		connection.close()
		self.table.resizeColumnsToContents()

	def changee(self):
		cout=999
		sender = self.sender()
		for i in range(self.n):
			if sender==self.btn7[i]:
				cout=i+1
				break
		os.system("python3 change.py "+str(cout))

if __name__ == '__main__':
    app = Qt.QApplication([])
    w = Widget(Qt.QTableWidget())
    sys.exit(app.exec_())
