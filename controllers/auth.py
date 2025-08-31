
import bcrypt
from models.usuario import Usuario
from config.database import get_connection
import mysql.connector

class AuthController:
    def __init__(self):
        self.get_connection = get_connection

    def conectar(self):
        return mysql.connector.connect(**self.get_connection)

    def registrar_usuario(self, usuario, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        connection = self.conectar()
        cursor = connection.cursor()
        query = "INSERT INTO Usuario (username, password_hash) VALUES (?, ?)"
        cursor.execute(query, (usuario, hashed))
        connection.commit()
        cursor.close()
        connection.close()

    def autenticar_usuario(self, usuario, password):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT password_hash FROM Usuario WHERE username = ?"
        cursor.execute(query, (usuario,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8'))
        return False
