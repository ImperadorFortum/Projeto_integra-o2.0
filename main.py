from PyQt5.QtWidgets import QApplication
import sys
from controller.ui_login import UiLogin 
import qdarkstyle
from qdarkstyle.light.palette import LightPalette


app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet(palette=LightPalette))                               
janela = UiLogin()
janela.show()
app.exec() #executar 
