import time
from os import system
from Front.Componentes.menuPrincipal import Menu
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

PIN_2 = 5
PIN_5 = 6
PIN_10 = 13
PIN_20 = 19
PIN_50 = 26
MONTANTE = 0

def atualiza_display(valor):
    telaDeMenu.tela_de_deposito.label_2.setText(f'R$ {MONTANTE},00')
    
try:
    import RPi.GPIO as gpio 
    def callback_2(chanel):
        global MONTANTE
        if gpio.input(PIN_2):
            telaDeMenu.tela_de_deposito.set_montante(2)
            telaDeMenu.tela_de_deposito.atualiza_display()

    def callback_5(chanel):
        global MONTANTE
        if gpio.input(PIN_5):
            telaDeMenu.tela_de_deposito.set_montante(5)
            telaDeMenu.tela_de_deposito.atualiza_display()

    def callback_10(chanel):
        global MONTANTE
        if gpio.input(PIN_10):
            telaDeMenu.tela_de_deposito.set_montante(10)
            telaDeMenu.tela_de_deposito.atualiza_display()

    def callback_20(chanel):
        global MONTANTE
        if gpio.input(PIN_20):
            telaDeMenu.tela_de_deposito.set_montante(20)
            telaDeMenu.tela_de_deposito.atualiza_display()      
    
    def callback_50(chanel):
        if gpio.input(PIN_50):
            telaDeMenu.tela_de_deposito.set_montante(50)
            telaDeMenu.tela_de_deposito.atualiza_display()

    gpio.setmode(gpio.BCM)
    gpio.setup(PIN_2, gpio.IN)
    gpio.setup(PIN_5, gpio.IN)
    gpio.setup(PIN_10, gpio.IN)
    gpio.setup(PIN_20, gpio.IN)
    gpio.setup(PIN_50, gpio.IN)
    gpio.add_event_detect(PIN_2, gpio.BOTH, callback=callback_2, bouncetime=100)
    gpio.add_event_detect(PIN_5, gpio.BOTH, callback=callback_5, bouncetime=100)
    gpio.add_event_detect(PIN_10, gpio.BOTH, callback=callback_10, bouncetime=100)
    gpio.add_event_detect(PIN_20, gpio.BOTH, callback=callback_20, bouncetime=100)
    gpio.add_event_detect(PIN_50, gpio.BOTH, callback=callback_50, bouncetime=100)

except:
    print('Runnig PC mode')

def deposito():
    while True:
        escolha = input('APERTE QUALQUER BOTÃO PARA ENCERRAR A OPERAÇÃO...\n').upper()
        if escolha:
            break
        time.sleep(0.5)

app = QtWidgets.QApplication([sys.argv])


while True:
    telaDeMenu = Menu()
    app.exec_()
exit()
