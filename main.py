from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from funcoes import somar, subtrair, dividir, multiplicar, porcentagem
from PyQt5.QtCore import pyqtSlot, QTimer


from os import path
import sys

def loadFile(file):
    base_path = getattr(sys, "_MEIPASS", path.dirname(path.abspath(__file__)))
    return path.join(base_path, file)

class MainUI(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi(loadFile("interface.ui"), self)
        self.show()


        self.num1 = 0
        self.num2 = 0
        self.finish = False

        self.selectedOperation = None
        self.operationList = {
            "+": somar,
            "-": subtrair,
            "x": multiplicar,
            "÷": dividir,
            "%": porcentagem
        }

        
        
        self.btn_1.clicked.connect(lambda : self.addNumber(1))
        self.btn_2.clicked.connect(lambda : self.addNumber(2))
        self.btn_3.clicked.connect(lambda : self.addNumber(3))
        self.btn_4.clicked.connect(lambda : self.addNumber(4))
        self.btn_5.clicked.connect(lambda : self.addNumber(5))
        self.btn_6.clicked.connect(lambda : self.addNumber(6))
        self.btn_7.clicked.connect(lambda : self.addNumber(7))
        self.btn_8.clicked.connect(lambda : self.addNumber(8))
        self.btn_9.clicked.connect(lambda : self.addNumber(9))
        self.btn_0.clicked.connect(lambda : self.addNumber(0))
        self.btn_virgula.clicked.connect(self.addComma)
        self.btn_ac.clicked.connect(self.cleanDisplay)
        self.btn_igual.clicked.connect(self.showResult)
        self.btn_maismenos.clicked.connect(self.reverseDisplay)
        
        self.btn_adicao.clicked.connect(lambda : self.setOperation("+"))
        self.btn_subtracao.clicked.connect(lambda : self.setOperation("-"))
        self.btn_multiplicacao.clicked.connect(lambda : self.setOperation("x"))
        self.btn_divisao.clicked.connect(lambda : self.setOperation("÷"))
        self.btn_porcento.clicked.connect(lambda : self.setOperation("%"))

    def timerClean(self):
        self.btn_adicao.setEnabled(False)
        self.btn_divisao.setEnabled(False)
        self.btn_subtracao.setEnabled(False)
        self.btn_multiplicacao.setEnabled(False)
        self.btn_porcento.setEnabled(False)
        self.btn_maismenos.setEnabled(False)
        self.btn_igual.setEnabled(False)
        self.btn_virgula.setEnabled(False)
        self.cronometro = QTimer(self)
        self.cronometro.timeout.connect(self.cleanDisplay)
        self.cronometro.singleShot(1000, self.cleanDisplay)
        self.cronometro.singleShot(1000, self.timeOutClean)

    def timeOutClean(self):
        self.btn_adicao.setEnabled(True)
        self.btn_divisao.setEnabled(True)
        self.btn_subtracao.setEnabled(True)
        self.btn_multiplicacao.setEnabled(True)
        self.btn_porcento.setEnabled(True)
        self.btn_maismenos.setEnabled(True)
        self.btn_igual.setEnabled(True)
        self.btn_virgula.setEnabled(True)
        self.resultado.setText("0")
        self.resultado2.setText("0")
        self.num1 = 0
        self.num2 = 0
        self.selectedOperation = None

    def addComma(self):
        ultimo = self.resultado.text()
        if ultimo.count(",") > 0:
            display = ultimo
        else:
            display = ultimo + ","
        self.resultado.setText(display) 

    def addNumber(self, numero):
        self.btn_ac.setText("<-")
        ultimo = self.resultado.text()
        if ultimo == '0' or self.finish:
            self.finish = False
            resultado = str(numero)
        else:
            resultado = ultimo + str(numero)
        self.resultado.setText(resultado)

    def cleanDisplay(self): 
        if self.btn_ac.text() == "AC":
            self.resultado.setText("0")
            self.resultado2.setText("0")
            self.num1 = 0
            self.num2 = 0
        else:
            ultimo = self.resultado.text()[:-1]
            if len(ultimo) == 0:
                ultimo = "0"
                self.btn_ac.setText("AC")
            self.resultado.setText(ultimo)

    def reverseDisplay(self):
        numero = self.getNumberDisplay(self.resultado)
        numero = str(numero * - 1)
        self.setNumberDisplay(numero)

    def percent(self):
        percent = self.getNumberDisplay(self.resultado)
        result = porcentagem(self.num1, percent)
        self.setNumberDisplay(result)       

    def setOperation(self, operation):
        self.selectedOperation = operation
        self.num1 = self.getNumberDisplay(self.resultado)
        self.num2 = 0
        result = self.resultado.text()
        self.resultado2.setText(result)
        self.resultado.setText("0")
        self.btn_ac.setText("AC")
        
    def getNumberDisplay(self, display):
        num = display.text()
        if "," in num:
            num = num.replace(',', '.')
            num = float(num)
        else:
            num = int(num)
        return num
    
    def setNumberDisplay(self, number):
        number = str(number)
        number = number.replace('.', ',')
        self.resultado.setText(number)

    def setCalcDisplay(self, num1, num2, operation):
        num1 = str(num1).replace('.',',')
        num2 = str(num2).replace('.',',')
        result = f'{num1} {operation} {num2} ='
        self.resultado2.setText(result)
        

    def showResult(self):
        if self.selectedOperation:
            if self.num2 == 0:
                self.num2 = self.getNumberDisplay(self.resultado)

            num1 = self.num1
            num2 = self.num2

            operation = self.operationList.get(self.selectedOperation)
            result = operation(num1, num2)
            self.num1 = result

            self.setNumberDisplay(result)
            self.setCalcDisplay(num1, num2, self.selectedOperation)
            self.btn_ac.setText("AC")
            self.finish = True
            if isinstance(result, str):
                self.timerClean()



