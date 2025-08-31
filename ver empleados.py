import sqlite3

conn = sqlite3.connect("proyecto.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Empleado")
empleados = cursor.fetchall()

for emp in empleados:
    print(emp)

cursor.close()
conn.close()
