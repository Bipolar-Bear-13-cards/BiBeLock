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
		layout.setAlignment(QtCore.Qt.AlignCenter)
		layout.addWidget(self.sprbtn)
		self.sprbtn.clicked.connect(self.showLog)
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
		self.show()
		self.Cuff()



	def selectAll(self):
		cout=0
		for i in range(len(self.allusr)):
			if self.sqr[i].isChecked():
				cout += 1
			self.sqr[i].setChecked(True)
		if cout==len(self.sqr):
			for i in range(len(self.allusr)):
				self.sqr[i].setChecked(False)

	def del_usr(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                    (UID TEXT, sname TEXT, name TEXT, mail TEXT, PIN TEXT, key TEXT)''')
		for sq in list(reversed(self.sqr)):
			if sq.isChecked():
				cursor.execute("DELETE FROM Users WHERE UID = ?",(self.allusr[self.sqr.index(sq)][0],))
		connection.commit()
		cursor.execute("SELECT * FROM Users")
		self.allusr=cursor.fetchall()
		self.table.setRowCount(len(self.allusr))
		connection.close()
		i=0;
		sqr=[]
		btn3=[]
		for oneusr in self.allusr:
			self.sqr.append(Qt.QCheckBox())
			self.sqr[i].setChecked(False)
			self.table.setCellWidget(i,0,self.sqr[i])
			self.btn3.append(Qt.QPushButton("подробнее"))
			self.table.setCellWidget(i, 6, self.btn3[i])
			self.btn3[i].clicked.connect(self.showLogOne)
			self.table.setItem(i, 1, QTableWidgetItem(oneusr[0]))
			self.table.setItem(i, 2, QTableWidgetItem(oneusr[1]))
			self.table.setItem(i, 3, QTableWidgetItem(oneusr[2]))
			self.table.setItem(i, 4, QTableWidgetItem(oneusr[3]))
			i+=1

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



	def showLogOne(self):
		cout=999
		sender = self.sender()
		for i in range(len(self.allusr)):
			if sender==self.btn3[i]:
				cout=i
				break
		os.system("python3 showLogOne.py "+self.allusr[cout][0])

	def showLog(self):
		os.system("python3 showLog.py")

	

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
		i=0
		for oneusr in self.allusr:
			cursor.execute("SELECT COUNT(*) FROM events WHERE UID=? AND sost=?", (oneusr[0],'1'))
			self.table.setItem(i, 5, QTableWidgetItem(str(cursor.fetchall()[0][0])))
			i += 1
		connection.close()
		self.table.resizeColumnsToContents()


if __name__ == '__main__':
    app = Qt.QApplication([])
    w = Widget(Qt.QTableWidget())
    sys.exit(app.exec_())

