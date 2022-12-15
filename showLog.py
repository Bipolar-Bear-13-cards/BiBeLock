from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import time
import sys



class Widget(Qt.QWidget):
	def __init__(self,table):
		super().__init__()
		timer = QtCore.QTimer(self, timeout=self.Cuff, interval=1000)
		timer.start()
		self.setWindowTitle("информация по неудачным попыткам входа")
		layout = Qt.QVBoxLayout(self)
		sprbtn=Qt.QPushButton("отметить все просмотренными")
		layout.addWidget(sprbtn)
		self.table = table
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
		cursor.execute("SELECT * FROM events")
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

	def Pomet(self):
		connection = sqlite3.connect('users.db')
		cursor = connection.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS events
                    (UID TEXT, dt TEXT, event TEXT, sost TEXT)''')
		cursor.execute("UPDATE events SET sost=?", ('0',))
		connection.commit()
		connection.close()


app = Qt.QApplication([])
w = Widget(Qt.QTableWidget())
sys.exit(app.exec_())

