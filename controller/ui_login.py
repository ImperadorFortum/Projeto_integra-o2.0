from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from controller.main_window import MainWindow


FILE_UI = 'view/ui_login.ui'

class UiLogin(QWidget):
    def __init__(self):
        super(UiLogin,self).__init__()
        uic.loadUi(FILE_UI,self)

        self.entrar.clicked.connect(self.Login)

    def Login(self):
        login = 'usuario'
        senha = 'senha'
        if login == 'usuario' and senha == 'senha' :
            self.label_4.setText("Entrando...")
            janela = MainWindow
            janela.show()
        else :
            self.label_4.setText("Dados de Login Incorretos!")
           
            
       



    






