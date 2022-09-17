from http import server
from db import connect
from .servicos import Servicos

class ServicosDAO():
    def add(c:Servicos):
        conn = connect()
        cursor = conn.cursor()
        SQL = "INSERT INTO Servicos(descricao,valor)VALUES(?,?)"
        dados =[c.descricao,c.valor]
        cursor.execute(SQL,dados)
        # pega o ID do ultimo selecionado
        id_return = cursor.execute("SELECT  last_insert_rowid();")
        id = id_return.fetchall()[0][0]
        
        conn.commit()
        conn.close()

        return id

    def edit(c:Servicos):
        conn = connect()    
        cursor = conn.cursor()
        SQL = "UPDATE Servicos SET descricao=?,valor=? WHERE id=?"
        dados = [c.id,c.descricao,c.valor]
        cursor.execute(SQL,dados)
        conn.commit()
        conn.close()

    def delete(id):
        print(id)
        conn = connect()
        cursor = conn.cursor()
        SQL = "DELETE FROM Servicos WHERE id=?;"
        cursor.execute(SQL,[id])
        conn.commit()
        conn.close()

    def selectAll() -> list:
        lista_consultas = []
        conn = connect()
        cursor = conn.cursor() 
        SQL = "SELECT* FROM Servicos;"
        cursor.execute(SQL)
        return_list = cursor.fetchall()  
        for c in return_list:
            #Obs: lembrar de pôr o ID no objeto Consulta
            nova_consulta = Servicos(c[0],c[1],c[2],)   
            lista_consultas.append(nova_consulta)

        conn.close()

        return lista_consultas
