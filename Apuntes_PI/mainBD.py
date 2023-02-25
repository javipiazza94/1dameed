import sqlite3

from miBase import creartabla
from miBase import crear_registro
from miBase import obtener_registros
from miBase import actualizar_registro
from miBase import eliminar_registro

# Definir los campos de la tabla
campos = [
    ('id', 'INTEGER PRIMARY KEY'),
    ('nombre', 'TEXT'),
    ('correo', 'TEXT')
]
"""
# Crear la tabla
creartabla('clientes', campos)

# Crear registros
crear_registro('clientes', (1, "Domin Targaryen", "kalboFollador@gmail.com"))
crear_registro('clientes', (2, "JaviPiazza", "javipiazza94@gmail.com"))

# Obtenermos los registros
print(obtener_registros('clientes'))

# Modificamos los registros
actualizar_registro('clientes', 2, ("Javi P. Piazza", "djIlpotroPiazza@gmail.com"), ['nombre', 'correo'])
print(obtener_registros('clientes')) 

#Eliminamos registros
eliminar_registro('clientes', 1)

"""
connect = sqlite3.connect('bd1.db')
cursor = connect.cursor()
filas = cursor.execute('SELECT * FROM clientes')
for row in filas:
    print(row)
cursor.close()
connect.close()






