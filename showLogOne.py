from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import sys
import time
import sqlite3




class Widget(Qt.QWidget):
	txt=[]
	def __init__(self,table):
		super().__init__()
		timer = QtCore.QTimer(self, timeout=self.Cuff, interval=1000)
		timer.start()
		self.setWindowTitle("информация по кодам доступа пользователя с id"+sys.argv[1])
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')
		cursor.execute("SELECT * FROM Users WHERE UID=?",(sys.argv[1],))
		self.events=cursor.fetchall()
		connection.close()
		self.table = table
		self.table.setRowCount(len(self.events))
		self.table.setColumnCount(2)
		self.table.setHorizontalHeaderLabels(["Время события","Тип события"])
		i=0
		for event in self.events:
			self.table.setItem(i, 1, QTableWidgetItem(event[1]))
			self.table.setItem(i, 2, QTableWidgetItem(event[2]))
			i += 1
		layout = Qt.QVBoxLayout(self)
		sprbtn1=Qt.QPushButton("сменить учётные данные")
		#sprbtn1.clicked.connect(self.deleteAll)
		layout.addWidget(sprbtn1)
		sprbtn=Qt.QPushButton("отметить все просмотренными")
		layout.addWidget(sprbtn)
		layout.addWidget(self.table)
		sprbtn.clicked.connect(self.Pomet)
		self.show()

	def Cuff(self):
		f=open(sys.argv[1]+"log")
		inlines=''
		f1=open(sys.argv[1]+"logCoutP")
		n=int(f1.read())
		f2=open(sys.argv[1]+"logCout")
		i=0
		for line in f:
			if i<n:
				inlines=(line+"\n"+inlines)
			else:
				inlines=("(новое)"+line+"\n"+inlines)
			i+=1
		if n+int(f2.read()) == 0:
			self.txt.setText("       Сообщений нет       ")
		else:
			self.txt.setText(inlines[:-1])
		f.close()
		f1.close()
		f2.close()

	def Pomet(self):
		f1=open(sys.argv[1]+"logCout")
		f1P=open(sys.argv[1]+"logCoutP")
		buffer=str(int(f1.read())+int(f1P.read()))
		f1.close()
		f1P.close()
		f1=open(sys.argv[1]+"logCout","w+")
		f1.write("0")
		f1.close()
		f2=open(sys.argv[1]+"logCoutP","w+")
		f2.write(buffer)
		f2.close()


app = Qt.QApplication([])
w = Widget(Qt.QTableWidget())
sys.exit(app.exec_())

