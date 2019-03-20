#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class Cronometro(QMainWindow):

    def __init__(self):
        super().__init__()
        
        uic.loadUi('cronowindow.ui', self)
        #self.show()
        self.pushButton.clicked.connect(self.clickedBntDefinir)
        self.pushButton.setCheckable(True)
    

    def getValueSpinSeg(self):
        return self.spinBoxSeg.value()
    
    def getValueSpinMin(self):
        return self.spinBoxMin.value()
    
    def clickedBntDefinir(self):
        if(self.pushButton.isChecked()):
            self.message = QMessageBox.about(self, 'Confi', 'As definições foram atualizadas')
            return True
