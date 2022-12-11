from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
import os
import sys



class Widget(Qt.QWidget):
    def __init__(self,table):
        super().__init__()
        self.setWindowTitle("  ")
        timer = QtCore.QTimer(self, timeout=self.Cuff, interval=1000)
        timer.start()
        layout1 = Qt.QVBoxLayout(self)
        txt1=Qt.QLabel("Приложите карту к считывателю")
        txt1.setAlignment(QtCore.Qt.AlignCenter)
        layout1.setAlignment(QtCore.Qt.AlignCenter)
        self.show()
        layout1.addWidget(txt1)
        self.Cuff()

    def Cuff(self):
        f = open("test","r")
        if(f.read[0:2]!="no"):
            self.close()
        f.close



app1 = Qt.QApplication([])
w1 = Widget(Qt.QTableWidget())
sys.exit(app1.exec_())
