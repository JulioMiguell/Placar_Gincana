# -*- coding: utf-8 -*-

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
import sys
import time
import threading
from random import randint
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLCDNumber, QVBoxLayout, 
QLabel, QPushButton, QSpinBox, QWidget, QHBoxLayout, QSizePolicy, QAbstractButton,
QLineEdit, QMessageBox)
from Cronometro import Cronometro

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.title = 'Placar para gincanas'
        self.top = 0
        self.left = 0
        self.width = 1366
        self.height = 650

        self.valorPlacarA = 0
        self.valorPlacarB = 0

        self.initWindow()
        self.cronoWindow = Cronometro()

    def initWindow(self):

        #espaço em branco
        espaco = QWidget()
        espaco.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        #Titulo do programa
        self.labelTituloJanela = QLabel(' PLACAR GINCANA', self)
        self.labelTituloJanela.setGeometry(450,10,430,100)
        self.labelTituloJanela.setStyleSheet('QLabel {font: 45px; color: white; font: bold; background-color: #19B5FE; border-radius: 10px}')

        #Seção dos LCDS
        self.lcdPlacar1 = QLCDNumber(self)
        self.lcdPlacar2 = QLCDNumber(self)
        self.lcdPlacar1.setGeometry(50, 120, 300, 250)
        self.lcdPlacar2.setGeometry(940, 120, 300, 250)
        self.lcdPlacar1.setStyleSheet('QLCDNumber {background-color: #000000; color: red; font: bold}')
        self.lcdPlacar1.setSegmentStyle(2) # QLCDNumber::SegmentStyle
        self.lcdPlacar2.setStyleSheet('QLCDNumber {background-color: #000000; color: red; font: bold}')
        self.lcdPlacar2.setSegmentStyle(2)

        #Label dos nomes dos grupos
        self.labelGrupA = QLabel('Grupo A', self)
        self.labelGrupB = QLabel('Grupo B', self)
        self.labelGrupA.setGeometry(125,20,200,100)
        self.labelGrupA.setStyleSheet('QLabel {font: 40px; font: bold;}')
        self.labelGrupB.setStyleSheet('QLabel {font: 40px; font: bold}')
        self.labelGrupB.setGeometry(1010,20,200,100)
        
        #Label do cronometro
        self.labelCrono = QLabel(' 00:00 ', self)
        self.labelCrono.setGeometry(130, 490, 170, 100)
        self.labelCrono.setStyleSheet('QLabel {background-color: #336E7B; color: white; font: 50px; border: None; border-radius: 20px}')

        #Label contendo a imagem central do programa
        self.imagemLabel = QLabel(self)
        pixmap = QPixmap('imagens/competir.png')
        self.imagemLabel.setPixmap(pixmap)
        self.imagemLabel.setGeometry(490,120,330,348)

        #Botões de pontuar os grupos
        self.bntGrupA = QPushButton('Pontuar Grupo A',self)
        self.bntGrupB = QPushButton('Pontuar Grupo B',self)
        self.bntGrupA.setGeometry(370,520,200,60)
        self.bntGrupB.setGeometry(690,520,200,60)
        self.bntGrupA.setStyleSheet('QPushButton {font: 23px; font: bold; background-color: #0AEB7E}')
        self.bntGrupB.setStyleSheet('QPushButton {font: 23px; font: bold; background-color: #0AEB7E}')

        #Spin para definir a pontução (Está entre os dois botões)
        self.spinBox = QSpinBox(self)
        self.spinBox.setMaximum(100)
        self.spinBox.setGeometry(592,520,90,60)
        self.spinBox.setStyleSheet('QSpinBox {font: 50px}')

        #Actions Buttons pontuação
        self.bntGrupA.clicked.connect(lambda: self.setValorLcd(1))
        self.bntGrupB.clicked.connect(lambda: self.setValorLcd(2))
        

            #Seção do cronômetro
        self.labelCronometro = QLabel('Cronometro', self)
        #self.labelCronometro.setIcon(QtGui.QIcon('crono'))
        self.labelCronometro.setStyleSheet('QLabel {font: 25px; color: black; font: bold; background-color: #ECF0F1;}')
        self.labelCronometro.setGeometry(145,440,150,50)

        self.bntIniciarCrono = QPushButton('INICIAR', self)
        self.bntIniciarCrono.setGeometry(130, 590, 185, 50)
        self.bntIniciarCrono.setStyleSheet('QPushButton {font: 20px; color: black; font: bold; background-color: #ECF0F1; border-radius: 10px}')
        self.bntIniciarCrono.setIcon(QtGui.QIcon('imagens/play'))
        self.bntIniciarCrono.setCheckable(True)
        self.bntIniciarCrono.clicked.connect(self.threadCrono)

            #Botão configurar cronometro
        self.bntConfingCronometro = QPushButton('Configurar', self)
        self.bntConfingCronometro.setGeometry(165, 650,100,50)
        self.bntConfingCronometro.setStyleSheet('QPushButton {font: 20px; color: black; font: bold; background-color: #ECF0F1; border-radius: 10px}')
        self.bntConfingCronometro.clicked.connect(self.configCronometro)
        
        #Seção Sortear Número
        self.labelSorteio = QLabel('Sortear Número',self)
        self.labelSorteio.setStyleSheet('QLabel {font: 25px; color: black; font: bold; background-color: #ECF0F1;}')
        self.labelSorteio.setGeometry(970, 450,200,50)
        self.labelAte = QLabel('ATÉ', self)
        self.labelAte.setStyleSheet('QLabel {font: 25px; color: black; font: bold; background-color: #ECF0F1;}')
        self.labelAte.setGeometry(1040,520,50,50)
        self.spinBoxNumb1 = QSpinBox(self)
        self.spinBoxNumb2 = QSpinBox(self)
        self.spinBoxNumb1.setGeometry(940, 520, 90, 50)
        self.spinBoxNumb2.setGeometry(1100, 520, 90, 50)
        self.spinBoxNumb1.setStyleSheet('QSpinBox {font: 50px}')
        self.spinBoxNumb2.setStyleSheet('QSpinBox {font: 50px}')
        self.bntSortear = QPushButton('Sortear', self)
        self.bntSortear.setGeometry(1020, 590,90,50)
        self.bntSortear.setStyleSheet('QPushButton {font: 25px; color: black; font: bold; background-color: #F9690E; border-radius: 10px}')
        self.bntSortear.clicked.connect(self.sortearNumero)
        
        #Seção da janela principal
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("user.png"))
        self.show()

    def setValorLcd(self,n):
        

        if (n == 1):
            self.lcdPlacar1.display(self.spinBox.value())
            self.valorPlacarA = self.spinBox.value()

        if(n == 2):
            self.lcdPlacar2.display(self.spinBox.value())
            self.valorPlacarB = self.spinBox.value()
        
        def placarColor(valorPlacarA, valorPlacarB):
            if (valorPlacarA > valorPlacarB):
                self.lcdPlacar1.setStyleSheet('QLCDNumber {background-color: #3FC380; color: white; font: bold}')
            
            if(valorPlacarB > valorPlacarA):
                self.lcdPlacar2.setStyleSheet('QLCDNumber {background-color: #3FC380; color: white; font: bold}')
            
            if(valorPlacarA < valorPlacarB):
                self.lcdPlacar1.setStyleSheet('QLCDNumber {background-color: #F22613; color: white; font: bold}')
            
            if(valorPlacarB < valorPlacarA):
                self.lcdPlacar2.setStyleSheet('QLCDNumber {background-color: #F22613; color: white; font: bold}')
                
            if(valorPlacarA == valorPlacarB):
                self.lcdPlacar1.setStyleSheet('QLCDNumber {background-color: #22A7F0; color: white; font: bold}')
                self.lcdPlacar2.setStyleSheet('QLCDNumber {background-color: #22A7F0; color: white; font: bold}')
           
            


        placarColor(self.valorPlacarA, self.valorPlacarB)       
    
    def bntIniciarCronoState(self):
        i = 0
        if (self.bntIniciarCrono.isChecked()):
            i += 1
            return i
        return i

    def threadCrono(self):
        global stop 
        stop = 0
        bntCronoStatus = self.bntIniciarCronoState()
        
        if (bntCronoStatus == 1):
            self.t = threading.Thread(target = self.iniciarCrono)
            self.bntIniciarCrono.setText('PARAR')
            self.t.start()

        if(bntCronoStatus == 0):
            self.bntIniciarCrono.setText('Iniciar novamente')
            stop = -1

    def iniciarCrono(self):
        
        self.seg = self.cronoWindow.getValueSpinSeg()
        self.min = self.cronoWindow.getValueSpinMin()
        
        self.count = 0
        self.i = self.seg + (self.min * 60)
    
        while (self.i != 0):
            self.min = self.count/60
            self.seg = self.count % 60 + 1
            time.sleep(1)
            self.labelCrono.setText('%02d:%02d' %(self.min, self.seg))
            self.count += 1
            self.i -= 1

            if stop == -1:
                self.bntIniciarCrono.setText('Iniciar novamente')
                self.i = 0
    
    def sortearNumero(self):
        try:
            a = self.spinBoxNumb1.value()
            b = self.spinBoxNumb2.value()
            self.resultado = randint(a,b)
            self.msgResultado = QMessageBox()
            self.msgResultado.setStyleSheet('QMessageBox, QMessageBox QLabel {font: 35px; color: white; background-color:#34495E}')
            self.msgResultado.information(self.msgResultado, 'INFORMAÇÃO ', 'Número sorteado:  \n-->{:>7}        <--'.format(self.resultado))
        except ValueError:
            self.warningValue = QMessageBox()
            self.warningValue.setStyleSheet('QMessageBox, QMessageBox QLabel {font: bold; color: white; font: 25px; background-color: #D91E18;}')
            self.warningValue.warning(self.warningValue, 'Aviso', 'Entrada incorreta! \n 1 até 0 é inválido' )
            
            
    
    def configCronometro(self):
        print('Inciando cronometro')
        self.cronoWindow = Cronometro()
        self.cronoWindow.show()
        
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
