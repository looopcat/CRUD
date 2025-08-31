# init_db.py
import sqlite3
from config.database import get_connection

def crear_tablas():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabla Departamento
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        gerente_id INTEGER
    )
    """)

    # Tabla Proyecto
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Proyecto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        fecha TEXT
    )
    """)

    # Tabla Empleado
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Empleado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        direccion TEXT,
        telefono TEXT,
        email TEXT,
        fecha_inicio TEXT,
        salario REAL,
        departamento_id INTEGER,
        proyecto_id INTEGER,
        rut TEXT,
        FOREIGN KEY(departamento_id) REFERENCES Departamento(id),
        FOREIGN KEY(proyecto_id) REFERENCES Proyecto(id)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Tablas creadas exitosamente.")

if __name__ == "__main__":
    crear_tablas()
