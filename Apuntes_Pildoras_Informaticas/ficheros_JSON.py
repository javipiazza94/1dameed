import json

#LEER JSON DESDE CARACTERES
datos_json='{"nombre":"carlos","edad":23}'
datos = json.loads(datos_json)
print(type(datos))
print(datos)

#LEER DESDE UN FICHERO
with open("ejemplo1.json") as fichero:
    datos2=json.load(fichero)
print(type(datos2))
print(datos2)

"""
    //El JSON describe una tienda de libros (bookstore) que contiene cuatro libros (book). Cada libro tiene varias propiedades como category (categoría del libro), price (precio), author (autor o autores), title (título del libro) y year (año de publicación).

//Cada libro tiene una propiedad title que a su vez tiene dos sub-propiedades __text y _lang. La sub-propiedad __text contiene el título del libro y la sub-propiedad _lang contiene el idioma del título.

//En el tercer libro, author es una lista de autores, en lugar de un solo autor.
"""

#CREAMOS UN FICHERO JSON Y LO ESCRIBIMOS

# Creamos un diccionario con el número de Grand Slams ganados por cada jugador del Big4
datos = {'Roger Federer': 20, 'Rafael Nadal': 20, 'Novak Djokovic': 20, 'Andy Murray': 3}

# Abrimos el archivo JSON en modo escritura
with open("big4_slams.json", "w") as fichero:
    # Escribimos los datos del diccionario en el archivo JSON
    json.dump(datos, fichero)
