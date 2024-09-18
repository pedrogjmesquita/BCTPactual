from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout
from Front.Componentes.telaDeDeposito import Deposito
import re
from PyQt5.QtWidgets import QMessageBox

class Menu(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setup_ui('MainPage')
        self.showFullScreen()

    def setup_ui(self, ui_name: str):

        uic.loadUi(r'Front/UIs/menuPrincipal.ui', self)
        
        self.tela_de_deposito = Deposito()
        self.label = QLabel(self, text="Chave PIX:", font=QtGui.QFont("Arial", 22))
        self.email_field = QLineEdit(self, placeholderText="Digite a chave PIX", font=QtGui.QFont("Arial", 22))
        self.proximo = QPushButton(self, text="Próximo", font=QtGui.QFont("Arial", 22))
        self.proximo.hide()
        self.label.hide()
        self.email_field.hide()
        
        self.startButton.clicked.connect(self.startOperacao)
        self.proximo.clicked.connect(self.comecaDeposito)
    
    def startOperacao(self):
        self.startButton.hide()
        self.verticalLayout = QVBoxLayout()
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.email_field)
        self.verticalLayout.addWidget(self.proximo)
        self.label.show()
        self.email_field.show()
        self.proximo.show()


    def comecaDeposito(self):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not re.match(email_regex, self.email_field.text()):
            self.email_field.setStyleSheet("border: 1px solid red;")
            self.wrong_email_warning()
            return
        else:
            self.tela_de_deposito.set_pix(self.email_field.text())
            self.tela_de_deposito.show()
            self.tela_de_deposito.reset_montante()
            self.tela_de_deposito.setFocus(True)
            self.tela_de_deposito.raise_()
            self.tela_de_deposito.showFullScreen()
            self.close()
            
    def wrong_email_warning(self):
        msg = QMessageBox()
        msg.setText(f'Email invalido! Por favor se certifique que está colocando um email válido')
        msg.addButton('Ok', QMessageBox.YesRole)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Email invalido")
        msg.exec_()