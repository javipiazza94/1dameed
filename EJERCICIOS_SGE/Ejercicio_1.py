# EJERCICIOS SGE
import re
import unicodedata
import os
from collections import Counter

print("-----------------------EJERCICIOS 1 Y 2 ---------------------------")

frase = "Estamos realizando la prueba de la función"
def contar_palabras_sin_acento(frase):
    frase = re.sub(r'[^\w\s]', ' ', frase)  # elimina cualquier signo de puntuación
    palabras = unicodedata.normalize('NFD', frase).encode('ascii', 'ignore').decode()
    print("La frase sin acento es: "+palabras)
    palabras = frase.split()
    return len(palabras)
print(frase)
print("La frase de prueba tiene "+str(contar_palabras_sin_acento(frase))+ " letras")

print("-----------------------EJERCICIOS 3 ---------------------------")

nombre_archivo = "Fichero para escribir.txt"
fichero = open(nombre_archivo, 'w')
texto ="Y yo me llamo Ralph"
fichero.write(texto)
fichero.close()

def contar_palabras_archivo(fichero):
    with open(nombre_archivo, 'r') as archivo:
        texto = archivo.read() #No es un void, debe de igualarse a una variable
        return contar_palabras_sin_acento(texto)

print("El numero de palabras en el documento es "+str(contar_palabras_archivo(fichero)))


print("-----------------------EJERCICIO 4 ---------------------------")

def contar_palabras_archivo_existe(nombre_archivo):
    if os.path.isfile(nombre_archivo):
        print(f"El archivo {nombre_archivo} si existe.")
        with open(nombre_archivo, 'r') as archivo:
            texto = archivo.read()
            return contar_palabras_sin_acento(texto)
    else:
        print(f"El archivo {nombre_archivo} no existe.")

print("Si el archivo existe su numero de palaras es " + str(contar_palabras_archivo_existe(nombre_archivo)))

print("-----------------------EJERCICIO 5 ---------------------------")

resultado = contar_palabras_archivo(nombre_archivo)
print(resultado)

print("-----------------------EJERCICIO 6 ---------------------------")

lista = ["a", "v", "Caesar"]
cadena = "Ave Caesar, los que van a morir te saludan"
def contar_ocurrencias(lista, cadena):
    ocurrencias = {}
    for palabra in lista:
        ocurrencias[palabra] = cadena.count(palabra)
    return ocurrencias
print("Las concurrencias de palabras en esta cadena son: "+str(contar_ocurrencias(lista, cadena)))

print("-----------------------EJERCICIO 7 ---------------------------")

def contar_ocurrencias_counter(lista, cadena):
    ocurrencias = contar_ocurrencias(lista, cadena)
    return Counter(ocurrencias)

print("Las concurrencias de palabras en esta cadena con Counter son: "+str(contar_ocurrencias_counter(lista, cadena)))

print("-----------------------EJERCICIO 8 ---------------------------")

nombre_archivo2 = "texto_ejemplo.txt"
lista_palabras2 = ["Si", "una", "mujer"]
fichero2 = open(nombre_archivo2, 'w')
texto2 ="Si una mujer tiene 1000 Me gusta y 500 comentarios en una foto, ¿Qué le falta? - ROPA"
fichero2.write(texto2)
texto2 = texto2.split()
fichero2.close()
def contar_ocurrencias_archivo(nombre_archivo2, lista_palabras2):
    with open(nombre_archivo2, 'r') as archivo:
        if os.path.isfile(nombre_archivo2):
            texto = archivo.read()
            return contar_ocurrencias(texto, lista_palabras2)

print("Las concurrencias de palabras en este archivo con Counter son: "+str(contar_ocurrencias_archivo(nombre_archivo2, lista_palabras2)))




