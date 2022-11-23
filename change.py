from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import sys





class Widget(Qt.QWidget):
	pole1=[]
	pole2=[]
	def __init__(self,table):
		super().__init__()
		self.setWindowTitle("Смена данных владельца участка №"+sys.argv[1])
		layout1 = Qt.QVBoxLayout(self)
		txt1=Qt.QLabel("Новая фамилия владельца:")
		self.pole1=Qt.QLineEdit()
		txt1.setAlignment(QtCore.Qt.AlignLeft)
		self.pole1.setAlignment(QtCore.Qt.AlignLeft) 
		txt2=Qt.QLabel("Новая электронная почта владельца:") 
		self.pole2=Qt.QLineEdit() 
		txt2.setAlignment(QtCore.Qt.AlignLeft) 
		self.pole2.setAlignment(QtCore.Qt.AlignLeft)
		layout1.addWidget(txt1)
		layout1.addWidget(self.pole1)
		layout1.addWidget(txt2)
		layout1.addWidget(self.pole2)
		self.show()
		sprbtn1=Qt.QPushButton("ОК")
		sprbtn1.clicked.connect(self.okk)
		sprbtn2=Qt.QPushButton("отмена")
		sprbtn2.clicked.connect(self.cancel)
		layout1.addWidget(sprbtn1)
		layout1.addWidget(sprbtn2)

	def okk(self):
		f=open(sys.argv[1]+"name","w+")
		f.write(self.pole1.text())
		f.close()
		f=open(sys.argv[1]+"mail","w+")
		f.write(self.pole2.text())
		f.close()
		self.close()

	def cancel(self):
		self.close()


app1 = Qt.QApplication([])
w1 = Widget(Qt.QTableWidget())
sys.exit(app1.exec_())
