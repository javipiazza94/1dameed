#Son las funciones predefinidas en Python. No hay necesidad de descargarlas porque ya vienen por defecto

lista = [1,2,3,4,5,6,7,8,9,10]
Nombres = ["Pepito", "Pepote", "Pepon", "Pep", "Papa", "Popitas"]

def Par(a):
    if a%2==0:
        return True
    return False

#Hacemos una funcion que devuelva los numeros pares

def Funcion_cadena(b):
    if str(b).startswith("Pep"):
        return True
    return False

#Hacemos una funcion que devuelve las palabras que empiezan por pep

resultado_numeros = filter(Par, lista) # En esta variable guardamos el filtro con la lista y la funcion 
resultado_cadena = filter(Funcion_cadena, Nombres)
#filter --> Aplica una funcion a todos los elementos de una lista
print(list(resultado_numeros))
print(list(resultado_cadena))