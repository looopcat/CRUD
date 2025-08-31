import sqlite3

# Nombre del archivo de base de datos SQLite
DB_NAME = "proyecto.db"

def get_connection():
    """
    Retorna una conexión a la base de datos SQLite.
    El archivo 'proyecto.db' se crea automáticamente si no existe.
    """
    connection = sqlite3.connect(DB_NAME)
    # Para obtener filas como diccionarios (opcional, muy útil):
    connection.row_factory = sqlite3.Row
    return connection

