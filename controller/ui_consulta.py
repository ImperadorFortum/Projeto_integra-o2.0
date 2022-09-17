from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

FILE_UI = 'view/ui_consulta.ui'

class UiConsulta(QWidget):
    
    def __init__ (self):
        super(UiConsulta,self). __init__()
        uic.loadUi(FILE_UI,self)