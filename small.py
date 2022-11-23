from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import sys
import random




class Widget(Qt.QWidget):
	def __init__(self,table):
		super().__init__()
		self.setWindowTitle("код для входа в общвую калитку для участка №"+sys.argv[1])
		f=open(sys.argv[1])
		txt=Qt.QLabel(f.readlines()[random.randint(0,5)][:-1],self)
		txt.setAlignment(QtCore.Qt.AlignCenter)
		layout = Qt.QHBoxLayout(self)
		layout.addWidget(txt)
		self.setMinimumSize(QSize(400, 30))
		self.show()



app = Qt.QApplication([])
w = Widget(Qt.QTableWidget())
sys.exit(app.exec_())
