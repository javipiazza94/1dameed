# EJERCICIOS SGE
import re
import unicodedata
import os
from collections import Counter

print("-----------------------EJERCICIOS 1 Y 2 ---------------------------")

frase = "Estamos realizando la prueba de la función"
def contar_palabras_sin_acento(frase):
    palabras = unicodedata.normalize('NFD', frase).encode('ascii', 'ignore').decode() #Ignoramos los signos de puntuacion
    print("La frase sin acento es: "+palabras) #(E2)
    palabras = frase.split() # Se convierte en una lista con las palabras
    return len(palabras) # devuelve el numero de palabras
print(frase)
print("La frase de prueba tiene "+str(contar_palabras_sin_acento(frase))+ " palabrass")

print("-----------------------EJERCICIOS 3 ---------------------------")

nombre_archivo = "Fichero para escribir.txt"
fichero = open(nombre_archivo, 'w')
texto ="Y yo me llamo Ralph"
fichero.write(texto)
fichero.close()

def contar_palabras_archivo(str):
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
def contar_ocurrencias(list, str): #Se pone como parametro el tipo de dato directamente
    ocurrencias = {}
    for palabra in list:
        ocurrencias[palabra] = str.count(palabra) 
    return ocurrencias
print("Las concurrencias de palabras en esta cadena son: "+str(contar_ocurrencias(lista, cadena)))

print("-----------------------EJERCICIOS 7, 8, 9, 10---------------------------")

def contar_ocurrencias_counter(list, str):
    if os.path.exists(str): #Ese String es el archivo que hemos creado. Llamamos a la libreria OS por si existe
        with open(str, 'r') as archivo: #Usamos la funcion open para abrir el archivo (E8)
            texto = archivo.read() #Usamos la funcion read para leerlo (E8)
            ocurrencias = contar_ocurrencias(list, str) 
        return Counter(ocurrencias) #CDevolvemos el objeto Counter con la ocurrencia (E7)
    else:
        print("Error: el archivo no existe.") #Mensaje de error por si el archivo no existe (E9)

resultado = contar_ocurrencias_counter(lista, nombre_archivo) #Llamamos a la funcion con una variable resultado
print(resultado) #(E10)



