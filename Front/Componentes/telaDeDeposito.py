from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class Deposito(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.montante = 0
        self.atualiza_display()
#        self.hide()

    def setup_ui(self):

        uic.loadUi('Front\\UIs\\telaDeDeposito.ui', self)

        self.pushButton_2.clicked.connect(self.cancelOperacao)
        self.pushButton.clicked.connect(self.confirmOperacao)
        
    def atualiza_display(self):
        self.label_2.setText(f'R${self.montante},00')
    
    def set_montante(self,valor):
        self.montante += valor
        self.atualiza_display()
        
    
    def reset_montante(self):
        self.montante = 0
        self.atualiza_display()
        
    def set_pix(self, pix):
        self.pix = pix
    
    def cancelOperacao(self):
        msg = QMessageBox()
        msg.setText('Deseja realmente cancelar a operação? Se você cancelar a operação, o dinheiro já depositado NÃO será devolvido.')
        msg.addButton('Sim', QMessageBox.YesRole)
        msg.addButton('Não', QMessageBox.NoRole)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Atenção")
        msg.exec_()
       
        resposta = msg.buttonRole(msg.clickedButton())
        if resposta == QMessageBox.YesRole:
            self.close()
        else:
            print('Operação cancelada')

    
    def confirmOperacao(self):
        msg = QMessageBox()
        msg.setText('Quer finalizar a transação?')
        msg.addButton('Sim', QMessageBox.YesRole)
        msg.addButton('Não', QMessageBox.NoRole)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Finalizar?")
        msg.exec_()
        
        resposta = msg.buttonRole(msg.clickedButton())
        if resposta == QMessageBox.YesRole:
            self.finalizaOperacao()
            self.close()
        else:
            pass
    
    def finalizaOperacao(self):
        msg = QMessageBox()
        msg.setText(f'PIX no valor de {self.montante} enviado para {self.pix}!')
        msg.addButton('Ok', QMessageBox.YesRole)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Operação finalizada")
        msg.exec_()