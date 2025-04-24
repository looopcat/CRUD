import mysql.connector
from models.empleado import Empleado
from config.database import db_config

class EmpleadoController:
    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def crear_empleado(self, empleado):
        connection = self.conectar()
        cursor = connection.cursor()
        query = """
        INSERT INTO Empleado (nombre, direccion, telefono, email, fecha_inicio, salario, departamento_id, rut, proyecto_id) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            empleado.get_nombre(),
            empleado.get_direccion(),  
            empleado.get_telefono(),
            empleado.get_email(),
            empleado.get_fecha_inicio(),
            empleado.get_salario(),
            empleado.get_departamento_id(),
            empleado.get_rut(),
            empleado.get_proyecto_id()
        ))
        connection.commit()
        cursor.close()
        connection.close()

    def listar_empleados(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT id, nombre FROM Empleado"
        cursor.execute(query)
        empleados = cursor.fetchall()
        cursor.close()
        connection.close()
        return empleados

    def buscar_empleado_por_id(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Empleado WHERE id = %s"
        cursor.execute(query, (id,))
        empleado = cursor.fetchone()
        cursor.close()
        connection.close()
        return empleado

    def modificar_empleado(self, empleado):
        connection = self.conectar()
        cursor = connection.cursor()
        query = """
        UPDATE Empleado 
        SET nombre = %s, direccion = %s, telefono = %s, email = %s, 
            fecha_inicio = %s, salario = %s, departamento_id = %s, rut = %s
        WHERE id = %s
        """
        cursor.execute(query, (
            empleado.get_nombre(),
            empleado.get_direccion(),
            empleado.get_telefono(),
            empleado.get_email(),
            empleado.get_fecha_inicio(),
            empleado.get_salario(),
            empleado.get_departamento_id(),
            empleado.get_rut(),
            empleado.get_id()
        ))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar_empleado(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM Empleado WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()

    def asignar_departamento(self, empleado_id, departamento_id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE Empleado SET departamento_id = %s WHERE id = %s"
        cursor.execute(query, (departamento_id, empleado_id))
        connection.commit()
        cursor.close()
        connection.close()

    def asignar_proyecto(self, empleado_id, proyecto_id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "UPDATE Empleado SET proyecto_id = %s WHERE id = %s"
        cursor.execute(query, (proyecto_id, empleado_id))
        connection.commit()
        cursor.close()
        connection.close()