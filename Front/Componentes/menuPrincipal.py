from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout
from Front.Componentes.telaDeDeposito import Deposito

class Menu(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setup_ui('MainPage')
        self.showFullScreen()

    def setup_ui(self, ui_name: str):

        uic.loadUi('Front\\UIs\\menuPrincipal.ui', self)
#         self.show()
        
        self.tela_de_deposito = Deposito()
        self.label = QLabel(self, text="Chave PIX:", font=QtGui.QFont("Arial", 22))
        self.textfield = QLineEdit(self, placeholderText="Digite a chave PIX", font=QtGui.QFont("Arial", 22))
        self.proximo = QPushButton(self, text="Próximo", font=QtGui.QFont("Arial", 22))
        self.proximo.hide()
        self.label.hide()
        self.textfield.hide()
        
        self.startButton.clicked.connect(self.startOperacao)
        self.proximo.clicked.connect(self.comecaDeposito)
    
    def startOperacao(self):
        self.startButton.hide()
        self.verticalLayout = QVBoxLayout()
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.textfield)
        self.verticalLayout.addWidget(self.proximo)
        self.label.show()
        self.textfield.show()
        self.proximo.show()


    def comecaDeposito(self):
        self.tela_de_deposito.set_pix(self.textfield.text())
        self.tela_de_deposito.show()
        self.tela_de_deposito.reset_montante()
        self.tela_de_deposito.setFocus(True)
        self.tela_de_deposito.raise_()
        self.tela_de_deposito.showFullScreen()
        self.close()
    