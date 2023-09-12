import sqlite3

#Creamos la base
conexion = sqlite3.connect('Qlite.db')

#Creamos el cursor
cursorDb = conexion.cursor()

#Creamos una tabla con sus columnas
cursorDb.execute("""CREATE TABLE estudiantes(
               Nombre TEXT,
               Edad INTEGER,
               Estatura REAL
)""")

#Insertamos datos
cursorDb.execute("""INSERT INTO estudiantes VALUES('Cesar Augusto', 27, 1.75)""") #Una fila
    #Creamos una lista con las tuplas(valores de los campos) de todos los datos que queremos añadir
datos = [
    ('Augusto', 27, 1.75), # fila 2
    ('Trajano', 101, 1.87), # fila 3
    ('Claudio', 45, 1.68), # fila 4
]
cursorDb.executemany("INSERT INTO estudiantes VALUES(?, ?, ?)", datos)

#Guardamos la tabla
conexion.commit()

#Vemos los datos
cursorDb.execute("SELECT * FROM estudiantes")
visualizar = cursorDb.fetchall()

for filas in visualizar:
    print(filas)


#Cerramos la conexion
conexion.close()