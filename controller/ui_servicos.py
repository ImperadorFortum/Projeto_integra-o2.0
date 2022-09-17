from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

FILE_UI = 'view/ui_servicos.ui'

class UiServicos(QWidget):

    def __init__(self):
        super(UiServicos,self). __init__()
        uic.loadUi(FILE_UI,self)