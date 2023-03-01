import shutil
import os

# Pedir al usuario las rutas de origen y destino
ruta_origen = input("Introduce la ruta de origen: ")
ruta_destino = input("Introduce la ruta de destino: ")

# Eliminar la carpeta de destino si existe
if os.path.exists(ruta_destino):
    shutil.rmtree(ruta_destino)

# Copiar la carpeta y su contenido
shutil.copytree(ruta_origen, ruta_destino)

