import sqlite3
from models.departamento import Departamento
from config.database import get_connection

class DepartamentoController:
    def __init__(self):
        pass

    def crear_departamento(self, departamento):
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO Departamento (nombre, gerente_id) VALUES (?, ?)"
        cursor.execute(query, (departamento.get_nombre(), departamento.get_gerente_id()))
        connection.commit()
        cursor.close()
        connection.close()

    def listar_departamentos(self):
        connection = get_connection()
        connection.row_factory = None 
        cursor = connection.cursor()
        query = "SELECT id, nombre, gerente_id FROM Departamento"
        cursor.execute(query)
        departamentos = cursor.fetchall()
        cursor.close()
        connection.close()

        return departamentos

    def buscar_departamento_por_id(self, id):
        connection = get_connection()
        connection.row_factory = None
        cursor = connection.cursor()
        query = "SELECT * FROM Departamento WHERE id = ?"
        cursor.execute(query, (id,))
        departamento = cursor.fetchone()
        cursor.close()
        connection.close()
        return departamento

    def modificar_departamento(self, departamento):
        connection = get_connection()
        connection.row_factory = None
        cursor = connection.cursor()
        query = "UPDATE Departamento SET nombre = ?, gerente_id = ? WHERE id = ?"
        cursor.execute(query, (departamento.get_nombre(), departamento.get_gerente_id(), departamento.get_id()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar_departamento(self, id):
        connection = get_connection()
        connection.row_factory = None
        cursor = connection.cursor()
        query = "DELETE FROM Departamento WHERE id = ?"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        
    def validar_id_departamento(self, departamento_id):
        cursor = self.connection.cursor()
        connection.row_factory = None
        query = "SELECT COUNT(*) FROM Departamento WHERE id = ?"
        cursor.execute(query, (departamento_id,))
        resultado = cursor.fetchone()[0]
        cursor.close()
        return resultado > 0