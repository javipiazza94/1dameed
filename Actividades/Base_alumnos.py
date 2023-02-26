import sqlite3

BD = "bd1.db"
def crear_tabla():
    # Conectarse a la base de datos
    conexion = sqlite3.connect(BD)
    cursor = conexion.cursor()
    # Crear la tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL
        );
    """)
    # Cerrar la conexión a la base de datos
    conexion.close()


def insertar_datos():
    # Conectarse a la base de datos
    conexion = sqlite3.connect(BD)
    cursor = conexion.cursor()
    # Verificar si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM Alumnos")
    count = cursor.fetchone()[0]
    if count == 0:
        # Insertar datos
        datos = [
            ("Ana", "González"),
            ("Juan", "Pérez"),
            ("María", "López"),
            ("Jorge", "Ruiz"),
            ("Laura", "García"),
            ("Carlos", "Martínez"),
            ("Marta", "Fernández"),
            ("Pedro", "Sánchez")
        ]
        cursor.executemany("INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)", datos)
        # Guardar los cambios y cerrar la conexión a la base de datos
        conexion.commit()
    # Cerrar la conexión a la base de datos
    conexion.close()


def buscar_alumno(nombre):
    # Conectarse a la base de datos
    conexion = sqlite3.connect(BD)
    cursor = conexion.cursor()
    # Buscar el alumno por nombre
    cursor.execute("SELECT * FROM Alumnos WHERE nombre=?", (nombre,))
    alumno = cursor.fetchone()
    if alumno:
        print(f"El alumno encontrado con los requisitos pedidos es: ID: {alumno[0]}, Nombre: {alumno[1]}, Apellido: {alumno[2]}")
    else:
        print("Alumno no encontrado.")
    # Cerrar la conexión a la base de datos
    conexion.close()

def obtener_registros():
    connect = sqlite3.connect('bd1.db')
    cursor = connect.cursor()
    cursor.execute(f"SELECT * FROM Alumnos")
    return cursor.fetchall()
    cursor.close()
    connect.close()

crear_tabla()
insertar_datos()
print(obtener_registros())
buscar_alumno("María")
