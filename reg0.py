from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import os


class Widget(Qt.QWidget):
    def __init__(self,table):
        super().__init__()
        txt1=Qt.QLabel("Приложите карту к считывателю")
        txt1.setAlignment(QtCore.Qt.AlignCenter)
        os.system("sudo python3 reg1.py")
        self.close()



app1 = Qt.QApplication([])
w1 = Widget(Qt.QTableWidget())
sys.exit(app1.exec_())
