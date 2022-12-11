from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import os


class Widget(Qt.QWidget):
    def __init__(self,table):
        super().__init__()
        layout1 = Qt.QVBoxLayout(self)
        txt1=Qt.QLabel("Ï")
        txt1.setAlignment(QtCore.Qt.AlignCenter)
        layout1.addWidget(txt1)
        os.system("sudo ./reg1.sh")
        self.close()



app1 = Qt.QApplication([])
w1 = Widget(Qt.QTableWidget())
sys.exit(app1.exec_())
