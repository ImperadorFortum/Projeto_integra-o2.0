from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QStatusBar
from PyQt5 import uic

from controller.ui_servicos import UiServicos
from controller.ui_consulta import UiConsulta



FILE_UI = 'view/main_window.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi(FILE_UI,self)

        self.pageConsulta = UiConsulta()
        self.pageServicos = UiServicos()
  

        self.stackedWidget.addWidget(self.pageConsulta)
        self.stackedWidget.addWidget(self.pageServicos)

        self.btnConsulta.clicked.connect(self.actionMenu)
        self.btnServicos.clicked.connect(self.actionMenu)
       
    def actionMenu(self):
        btn = self.sender()
        nomeBtn = btn.objectName()
        if nomeBtn == 'btnConsulta':
            self.stackedWidget.setCurrentIndex(0)
            

        if nomeBtn == 'btnServicos':
            self.stackedWidget.setCurrentIndex(1)
       
       

        
       
