from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

FILE_UI = 'view/ui_login.ui'

class UiDespesas(QWidget):

    def  __init__(self):
        super(UiDespesas,self). __init__()
        uic.loadUi(FILE_UI,self)