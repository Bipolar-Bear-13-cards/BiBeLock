from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize#, QColor
import sys
import time




class Widget(Qt.QWidget):
	table=[]
	def __init__(self,table):
		super().__init__()
		timer = QtCore.QTimer(self, timeout=self.Cuff, interval=1000)
		timer.start()
		self.setWindowTitle("информация по кодам доступа участка №"+sys.argv[1])
		self.table=table
		layout = Qt.QHBoxLayout(self)
		self.table.setRowCount(0)
		self.table.setColumnCount(3)
		self.table.setHorizontalHeaderLabels(["дата","время", "описание события"])
		sprbtn=Qt.QPushButton("отметить все просмотренными")
		layout.addWidget(self.table)
		layout.addWidget(sprbtn)
		sprbtn.clicked.connect(self.Pomet)
		self.show()

	def Cuff(self):
		f=open(sys.argv[1]+"log")
		inlines=''
		f1=open(sys.argv[1]+"logCoutP")
		n=int(f1.read())
		f2=open(sys.argv[1]+"logCout")
		i=0
		self.table.insertRow(2)
		self.table.setItem(0, 0, QTableWidgetItem(str(0)))
		for line in f:
			if i<n:
				inlines=(line+"\n"+inlines)
			else:
				inlines=("(новое)"+line+"\n"+inlines)
			i+=1
		#if n+int(f2.read()) == 0:
			#self.txt.setText("       Сообщений нет       ")
		#else:
			#self.txt.setText(inlines[:-1])
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

