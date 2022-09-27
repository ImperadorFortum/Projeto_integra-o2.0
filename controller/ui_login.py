from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

FILE_UI = 'view/ui_login.ui'

class UiLogin(QWidget):
    def __init__(self):
        super(UiLogin,self).__init__()
        uic.loadUi(FILE_UI,self)

        self.entrar.clicked.connect(self.login)

def login(self):
    login = 'valnormal123'
    senha = '210998lipe'
    if login == "login" and senha == "senha" :
        self.label_4.setText("Entrando...")
    else :
        self.label_4.setText("Dados de Login Incorretos!")
        
       



    






