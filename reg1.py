import os
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import sys





class Widget(Qt.QWidget):
	pole1=[]
	pole2=[]
	pole3=[]
	def __init__(self,table):
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
		f=open("test","w+")

	def cancel(self):
		f=open("test","w+")

	def small(self):
		os.system("python3 small.py "+str(1))

	def bigger(self):
		1

f=open("test","w+")
f.write("ye")
f.close()
app1 = Qt.QApplication([])
w1 = Widget(Qt.QTableWidget())
sys.exit(app1.exec_())
