import mysql.connector
from models.proyecto import Proyecto
from config.database import db_config

class ProyectoController:
    def __init__(self):
        self.db_config = db_config
        self.connection = self.conectar()

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def crear_proyecto(self, proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "INSERT INTO Proyecto (nombre, descripcion, fecha) VALUES (%s, %s, %s)"
        cursor.execute(query, (proyecto.get_nombre(), proyecto.get_descripcion(), proyecto.get_fecha()))
        connection.commit()
        cursor.close()
        connection.close()

    def listar_proyectos(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT id, nombre FROM Proyecto"
        cursor.execute(query)
        proyectos = cursor.fetchall()
        cursor.close()
        connection.close()
        #Crear la tabla formateada
        ##tabla = "| ID | Departamento | ID Gerente |\n"
        ##tabla += "|----|--------------|-----------|\n"
        
        """for dep in proyectos:
            tabla += f"| {dep[0]:<2} | {dep[1]:<12} | {dep[2] or 'N/A':<9} |\n"
        return tabla"""
        return proyectos

    def buscar_proyecto_por_id(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Proyecto WHERE id = %s"
        cursor.execute(query, (id,))
        proyecto = cursor.fetchone()
        cursor.close()
        connection.close()
        return proyecto

    def modificar_proyecto(self, proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE Proyecto SET nombre = %s, descripcion = %s, fecha =%s WHERE id = %s"
        cursor.execute(query, (proyecto.get_nombre(), proyecto.get_descripcion(), proyecto.get_fecha()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar_proyecto(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM Proyecto WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()

    def asignar_empleado(self, empleado_id, proyecto_id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE Empleado SET empleado_id = %s WHERE id = %s"
        cursor.execute(query, (empleado_id, proyecto_id))
        connection.commit()
        cursor.close()
        connection.close()
    
    def validar_id_proyecto(self, proyecto_id):
        cursor = self.connection.cursor()
        query = "SELECT COUNT(*) FROM Proyecto WHERE id = %s"
        cursor.execute(query, (proyecto_id,))
        resultado = cursor.fetchone()[0]
        cursor.close()
        return resultado > 0