import sqlite3
from models.proyecto import Proyecto
from config.database import get_connection

class ProyectoController:
    def __init__(self):
        pass

    def conectar(self):
        return get_connection()

    def crear_proyecto(self, proyecto):
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO Proyecto (nombre, descripcion, fecha) VALUES (?, ?, ?)"
        cursor.execute(query, (proyecto.get_nombre(), proyecto.get_descripcion(), proyecto.get_fecha()))
        connection.commit()
        cursor.close()
        connection.close()

    def listar_proyectos(self):
        connection = get_connection()
        connection.row_factory = None
        cursor = connection.cursor()
        query = "SELECT id, nombre FROM Proyecto"
        cursor.execute(query)
        proyectos = cursor.fetchall()
        cursor.close()
        connection.close()
        return proyectos

    def buscar_proyecto_por_id(self, id):
        connection = get_connection()
        connection.row_factory = None
        cursor = connection.cursor()
        query = "SELECT * FROM Proyecto WHERE id = ?"
        cursor.execute(query, (id,))
        proyecto = cursor.fetchone()
        cursor.close()
        connection.close()
        return proyecto

    def modificar_proyecto(self, proyecto):
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE Proyecto SET nombre = ?, descripcion = ?, fecha =? WHERE id = ?"
        cursor.execute(query, (proyecto.get_nombre(), proyecto.get_descripcion(), proyecto.get_fecha(), proyecto.get_id()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar_proyecto(self, id):
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM Proyecto WHERE id = ?"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()

    def asignar_empleado(self, empleado_id, proyecto_id):
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE Empleado SET empleado_id = ? WHERE id = ?"
        cursor.execute(query, (empleado_id, proyecto_id))
        connection.commit()
        cursor.close()
        connection.close()
    
    def validar_id_proyecto(self, proyecto_id):
        cursor = self.connection.cursor()
        connection.row_factory = None
        query = "SELECT COUNT(*) FROM Proyecto WHERE id = ?"
        cursor.execute(query, (proyecto_id,))
        resultado = cursor.fetchone()[0]
        cursor.close()
        return resultado > 0