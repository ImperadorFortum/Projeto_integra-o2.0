from PyQt5.QtWidgets import QApplication
import sys
from controller.ui_login import UiLogin

app = QApplication(sys.argv)
janela = UiLogin()
janela.show()
app.exec() 
