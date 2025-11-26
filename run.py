from PyQt5.QtWidgets import QApplication
from main import MainUI


if __name__== "__main__":
    app = QApplication([])
    tela = MainUI()
    app.exec_()