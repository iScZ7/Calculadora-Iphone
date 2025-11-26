from PyQt5.QtWidgets import QMainWindow, QShortcut
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from funcoes import somar

class MainUI(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi("interface.ui", self)
        self.show()

        
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
        self.btn_adicao.clicked.connect(self.setOperation)
        self.btn_subtracao.clicked.connect(self.setOperation)
        self.btn_multiplicacao.clicked.connect(self.setOperation)
        self.btn_divisao.clicked.connect(self.setOperation)


    def addComma(self):
        ultimo = self.resultado.text()
        if ultimo.count(",") > 0:
            display = ultimo
        else:
            display = ultimo + ","
        self.resultado.setText(display) 


    def addNumber(self, numero):
        a = self.resultado.text()
        if a == '0':
            resultado = str(numero)
        else:
            resultado = a + str(numero)
        self.resultado.setText(resultado)

    def cleanDisplay(self): 
        self.resultado.setText("0")

    def setOperation(self):
        result = self.resultado.text()
        self.resultado2.setText(result)
        self.cleanDisplay()
        
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
        result = f'{num1} {operation} {num2}'
        self.resultado2.setText(result)
        

    def showResult(self):
        num1 = self.getNumberDisplay(self.resultado)
        num2 = self.getNumberDisplay(self.resultado2)

        result = somar(num1, num2)
        self.setNumberDisplay(result)
        self.setCalcDisplay(num1, num2, "+")



