from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import sys
import random




class Widget(Qt.QWidget):
	def __init__(self,table):
		super().__init__()
		self.setWindowTitle("ПИН-код для пользователя с ID "+sys.argv[1])
		PIN=""
		for i in range(4):
			PIN=PIN+str(random.randrange(10))
		#здесь должна быть запись в базу данных пин-кода
		txt=Qt.QLabel(PIN)
		self.fontD = self.font()
		self.fontD.setPointSize(20)
		txt.setAlignment(QtCore.Qt.AlignCenter)
		txt.setFont(self.fontD) 
		layout = Qt.QHBoxLayout(self)
		layout.addWidget(txt)
		self.setMinimumSize(QSize(400, 30))
		self.show()



app = Qt.QApplication([])
w = Widget(Qt.QTableWidget())
sys.exit(app.exec_())
