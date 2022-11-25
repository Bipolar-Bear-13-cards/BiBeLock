from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import Qt, QtWidgets, QtCore
from PyQt5.QtCore import QSize
import sys
import time
import os
import random


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
	def __init__(self,table,n):
		super().__init__()
		self.n=n
		self.setWindowTitle("панель управления калиткой №1")
		self.sprbtn=Qt.QPushButton()
		timer = QtCore.QTimer(self, timeout=self.Cuff, interval=5000)
		timer.start()
		self.table = table
		layout = Qt.QVBoxLayout(self)		
		self.table.setRowCount(self.n)
		self.table.setColumnCount(9)
		self.table.setHorizontalHeaderLabels(["","Номер участка", "Фамилия владельца", "E-mail влодельца"," "," "," "," "," "])
		for i in range(self.n):
			self.sqr.append(Qt.QCheckBox())
			self.table.setCellWidget(i,0,self.sqr[i])
			self.btn3.append(Qt.QPushButton())
			self.table.setCellWidget(i, 4, self.btn3[i])
			self.btn3[i].clicked.connect(self.showLogOne)
			self.btn4.append(Qt.QPushButton("удалить все сообщения о событиях"))
			self.btn4[i].clicked.connect(self.deleteAllOne)
			self.table.setCellWidget(i, 5, self.btn4[i])
			self.btn5.append(Qt.QPushButton("сгенерировать новые коды входа"))
			self.btn5[i].clicked.connect(self.NewCode)
			self.table.setCellWidget(i, 6, self.btn5[i])
			self.btn6.append(Qt.QPushButton("выдать код входа"))
			self.btn6[i].clicked.connect(self.small)
			self.table.setCellWidget(i, 7, self.btn6[i])
			self.btn7.append(Qt.QPushButton("Сменить данные владельца"))
			self.btn7[i].clicked.connect(self.changee)
			self.table.setCellWidget(i, 8, self.btn7[i])
		layout.setAlignment(QtCore.Qt.AlignCenter)
		layout.addWidget(self.sprbtn)
		self.sprbtn.clicked.connect(self.showLog)
		sprbtn1=Qt.QPushButton("очистить историю неудачных попыток входа")
		sprbtn1.clicked.connect(self.deleteAll)
		layout.addWidget(sprbtn1)
		sprbtn2=Qt.QPushButton("выделить все")
		sprbtn2.clicked.connect(self.selectAll)
		layout.addWidget(sprbtn2)
		layout.addWidget(self.table)
		self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) 
		self.table.verticalHeader().setVisible(False)
		self.setMinimumSize(QSize(1300, 50))
		self.showMaximized() 
		self.Cuff()

	def deleteAll(self):
		os.system("python3 deleteAll.py")

	def selectAll(self):
		for i in range(self.n):
			self.sqr[i].setChecked(True)

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
		for i in range(self.n):
			if sender==self.btn3[i]:
				cout=i+1
				break
		os.system("python3 showLogOne.py "+str(cout))

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

	def small(self):
		cout=999
		sender = self.sender()
		for i in range(self.n):
			if sender==self.btn6[i]:
				cout=i+1
				break
		os.system("python3 small.py "+str(cout))

	def Cuff(self):
		f=open("logCout")
		self.sprbtn.setText(f.read()+" новых неудачных попыток(-ки) входа")
		f.close()
		for i in range (1,self.n+1):
			self.table.setItem(i-1, 1, QTableWidgetItem(str(i)))
			f=open(str(i)+"name")
			self.table.setItem(i-1, 2, QTableWidgetItem(f.read()))
			f.close()
			f=open(str(i)+"mail")
			self.table.setItem(i-1, 3, QTableWidgetItem(f.read()))
			f.close()
			f=open(str(i)+"logCout")
			self.btn3[i-1].setText(f.read()+" новых события(-й)")
			f.close()
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
    w = Widget(Qt.QTableWidget(),2)
    sys.exit(app.exec_())
