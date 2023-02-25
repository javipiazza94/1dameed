import sqlite3

BD = "bd1.db"
def creartabla(tabla, campos):
    #Actualiza los valores del registro con el ID especificado en la tabla indicada.
    # Conectarse a la base de datos
    conexion = sqlite3.connect(BD)
    cursor = conexion.cursor()
    campos_str = ', '.join([f"{campo[0]} {campo[1]}" for campo in campos])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {tabla} ({campos_str})")
    # Cerrar la conexión a la base de datos
    conexion.close()

def crear_registro(tabla, valores):
    #Actualiza los valores del registro con el ID especificado en la tabla indicada.
    # Conectarse a la base de datos
    conexion = sqlite3.connect(BD)
    cursor = conexion.cursor()
    valores_str = ', '.join('?' * len(valores))
    cursor.execute(f"INSERT INTO {tabla} VALUES ({valores_str})", valores)
    conexion.commit()
    # Cerrar la conexión a la base de datos
    conexion.close()

def obtener_registros(tabla, filtro=None):
   #Actualiza los valores del registro con el ID especificado en la tabla indicada.
    # Conectarse a la base de datos
    conexion = sqlite3.connect(BD)
    cursor = conexion.cursor()
    if filtro:
        cursor.execute(f"SELECT * FROM {tabla} WHERE {filtro}")
    else:
        cursor.execute(f"SELECT * FROM {tabla}")
    # Cerrar la conexión a la base de datos
    return cursor.fetchall()
    conexion.close()


def actualizar_registro(tabla, id_registro, nuevos_valores, campos):
   
    #Actualiza los valores del registro con el ID especificado en la tabla indicada.
    # Conectarse a la base de datos
    conexion = sqlite3.connect(BD)
    cursor = conexion.cursor()
    nuevos_valores = nuevos_valores + (id_registro,)
    nuevos_valores_str = ', '.join([f"{campo} = ?" for campo in campos])
    cursor.execute(f"UPDATE {tabla} SET {nuevos_valores_str} WHERE id = ?", nuevos_valores)
    conexion.commit()
    # Cerrar la conexión a la base de datos
    conexion.close()


def eliminar_registro(tabla, id_registro):
   #Actualiza los valores del registro con el ID especificado en la tabla indicada.
    # Conectarse a la base de datos
    conexion = sqlite3.connect(BD)
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM {tabla} WHERE id = ?", (id_registro,))
    conexion.commit()
    # Cerrar la conexión a la base de datos
    conexion.close()





