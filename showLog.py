from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import time
import sys
import sqlite3



class Widget(Qt.QWidget):
	def __init__(self,table):
		super().__init__()
		timer = QtCore.QTimer(self, timeout=self.Cuff, interval=1000)
		timer.start()
		self.setWindowTitle("информация по неудачным попыткам входа")
		layout = Qt.QVBoxLayout(self)
		sprbtn=Qt.QPushButton("отметить все просмотренными")
		layout.addWidget(sprbtn)
		sprbtn1=Qt.QPushButton("очистить историю попыток входа")
		sprbtn1.clicked.connect(self.deleteAll)
		layout.addWidget(sprbtn1)
		self.table = table
		layout.addWidget(self.table)
		sprbtn.clicked.connect(self.Pomet)
		self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) 
		self.table.verticalHeader().setVisible(False)
		self.setMinimumSize(QSize(700, 700))
		self.show()

	def Cuff(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')
		cursor.execute("SELECT * FROM events")
		self.events=cursor.fetchall()
		connection.close()
		self.table.setRowCount(len(self.events))
		self.table.setColumnCount(4)
		self.table.setHorizontalHeaderLabels(["Состояние","UID","Время события","Тип события"])
		i=0
		for event in self.events:
			if event[3]=='0':
				sost="просмотрено"
			else:
				sost="новое"
			self.table.setItem(i, 0, QTableWidgetItem(sost))
			self.table.setItem(i, 1, QTableWidgetItem(event[0]))
			self.table.setItem(i, 2, QTableWidgetItem(event[1]))
			self.table.setItem(i, 3, QTableWidgetItem(event[2]))
			i += 1
		self.table.resizeColumnsToContents()

	def Pomet(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')
		cursor.execute("UPDATE events SET sost=?", ('0',))
		connection.commit()
		connection.close()


	def deleteAll(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')
		cursor.execute("DROP TABLE events")
		connection.commit()
		connection.close()


app = Qt.QApplication([])
w = Widget(Qt.QTableWidget())
sys.exit(app.exec_())

