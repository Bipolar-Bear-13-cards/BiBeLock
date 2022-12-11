from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
import os
import sys



class Widget(Qt.QWidget):
    def __init__(self,table):
        super().__init__()
        timer = QtCore.QTimer(self, timeout=self.Cuff, interval=1000)
        timer.start()
        layout1 = Qt.QVBoxLayout(self)
        self.fontD = self.font()
        self.fontD.setPointSize(20)
        txt1=Qt.QLabel("Приложите карту к считывателю")
        txt1.setAlignment(QtCore.Qt.AlignCenter)
        self.txt1.setFont(self.fontD) 
        layout1.setAlignment(QtCore.Qt.AlignCenter)
        self.setMinimumSize(QSize(300, 40))
        self.show()
        layout1.addWidget(txt1)
        self.Cuff()

    def Cuff(self):
        f = open("test","r")
        if(f.read()[0:2]!="no"):
            self.close()
        f.close



app1 = Qt.QApplication([])
w1 = Widget(Qt.QTableWidget())
sys.exit(app1.exec_())
