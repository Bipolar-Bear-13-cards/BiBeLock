from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import sys
import time




class Widget(Qt.QWidget):
	txt=[]
	def __init__(self,table):
		super().__init__()
		timer = QtCore.QTimer(self, timeout=self.Cuff, interval=1000)
		timer.start()
		self.setWindowTitle("информация по кодам доступа участка №"+sys.argv[1])
		self.txt=Qt.QLabel('',self)
		self.txt.setAlignment(QtCore.Qt.AlignCenter)
		layout = Qt.QHBoxLayout(self)
		sprbtn=Qt.QPushButton("отметить все просмотренными")
		layout.addWidget(self.txt)
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
