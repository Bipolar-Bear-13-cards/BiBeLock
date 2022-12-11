from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import sys





class Widget(Qt.QWidget):
	pole1=[]
	pole2=[]
	pole3=[]
	def __init__(self,table):
		super().__init__()
		self.setWindowTitle("���������� ������ ������������")
		layout1 = Qt.QVBoxLayout(self)
		txt1=Qt.QLabel("�������:")
		self.pole1=Qt.QLineEdit()
		txt1.setAlignment(QtCore.Qt.AlignLeft)
		self.pole1.setAlignment(QtCore.Qt.AlignLeft) 
		txt2=Qt.QLabel("���:") 
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
		sprbtn1=Qt.QPushButton("��")
		sprbtn1.clicked.connect(self.okk)
		sprbtn2=Qt.QPushButton("������")
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
