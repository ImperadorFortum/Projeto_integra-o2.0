from PyQt5.QtWidgets import QWidget, QTableWidgetItem,QHeaderView
from PyQt5 import uic

from model.servicos import Servicos,Editar
from model.servicos_dao import ServicosDAO

FILE_UI = 'view/ui_servicos.ui'

class UiServicos(QWidget):

    def __init__(self):
        super(UiServicos,self). __init__()
        uic.loadUi(FILE_UI,self)

        self.addBtn.clicked.connect(self.add)
        self.editBtn.clicked.connect(self.edit)
        self.delBtn.clicked.connect(self.delete)
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        

        self.loadData()

    def loadData(self):
        listaCon = ServicosDAO.selectAll()
        for c in listaCon:
            self.addTableWidget(c)

    def add(self):
        lineSel = self.tabela.currentRow()
        id = self.tabela.item(lineSel,0)
        descricao = self.tabela.item(lineSel,1)
        valor = self.tabela.item(lineSel,2)
        
        novoServico = Servicos(-1,descricao,valor)
        id = ServicosDAO.add(novoServico)
        novoServico.id = id
        self.addTableWidget(novoServico)

        self.descricao.clear()
        self.valor.clear()

    def edit(self):
        lineSel = self.tabela.currentRow()
        id = self.tabela.item(lineSel,0)
        n_descricao = self.tabela.item(lineSel,1)
        n_valor = self.tabela.item(lineSel,2)

        n_descricao = self.descricao.text()
        n_valor = self.valor.text()

        edit = Servicos(id.text(),n_valor,n_descricao)
        self.edicao(edit)
        ServicosDAO.edit(edit)
        
        self.descricao.clear()
        self.valor.clear()
 
    def delete(self):
        # pega a linha
        lineSel = self.tabela.currentRow()

        item = self.tabela.item(lineSel,0) 
        id = item.text()
        print(id)
        # remove do banco
        ServicosDAO.delete(id) 
        # remove a linha 
        self.tabela.removeRow(lineSel)        
        
    def addTableWidget(self,c: Servicos):
        line = self.tabela.rowCount()
        self.tabela.insertRow(line)
        id = QTableWidgetItem(str(c.id))
        descricao = QTableWidgetItem(c.descricao)
        valor = QTableWidgetItem(c.valor)
        
        self.tabela.setItem(line, 0, id)
        self.tabela.setItem(line,1, descricao)
        self.tabela.setItem(line,2, valor)

    def edicao(self,c: Editar):
        lineSel = self.tabela.currentRow()
        n_id = QTableWidgetItem(c.id)
        n_descricao = QTableWidgetItem(c.descricao)
        n_valor = QTableWidgetItem(c.valor)
    
        self.tabela.item(lineSel, 0, n_id)
        self.tabela.item(lineSel, 1, n_descricao)
        self.tabela.item(lineSel, 2, n_valor)    