#Todos los tipos son objetos en Python
#VARIABLES Y TIPOS DE DATOS EN PYHTON
numeros = '5'
cadenas = "hola"
booleano = True
flotantes = '345.345'
listas = ['a', 'b', 'c']
    #metodos = .append(anade)
               #.remove(borra)
               #lista_ordenada = sorted(nombre_lista)
               #lista_ordenada = sorted(nombre_lista, reverse=True) --> Lo hace segun el codigo ASCII
tuplas = ('a', 'b', 'c')
diccionario = {'cadena' : '1'} #clave ->valor/ La clave es una cadena y el valor cualquier tipo de dato
    #metodos = .pop/del (borran)
conjunto = {'1', '2', '3', '1', '2', '3', '4', '5', '6'}
    #metodos = listaA|ListaB (Une conjuntos)
               #ListaA&ListaB (Hace intersecciones de valores comunes)
               #ListaA-ListaB (Hace diferencia de valores distintos)
rango = range(1,100) 
#VARIABLES IMPRESAS
print(numeros)
print(cadenas) 
print(booleano)
print(listas)
print(tuplas) 
print(diccionario)
print(conjunto)  
print(rango)           

#TEXTOS Y METODOS
Mitexto = "Ave Caesar, los que van a morir te saludaN"
print(Mitexto)
Mitexto.capitalize() #Pone en mayusculas la primera letra
print(Mitexto.capitalize())
Mitexto.title()#Pone en Mayusculas la primera letra de cada cadena
print(Mitexto.title())
Mitexto.lower() #Las pones todas en minuscula
print(Mitexto.lower())
Mitexto.upper() #Las pones todas en mayuscula
print(Mitexto.upper())
Mitexto.replace('u', 'v')#Reemplaza una letra por la otra
print(Mitexto.replace('u', 'v'))
Mitexto.find('Caesar') #Me dice en que posicion de memoria aparece la cadena
print(Mitexto.find('Caesar'))
Mitexto.split() # Convierte cada cadena del texto en una posicion de una lista
print(Mitexto.split())
' '.join(Mitexto)
#Se pueden concatenar metodos entre si
#Se pueden convertir listas en cadenas al poner el metodo join con una cadena vacia ' '.join(nombrelista)

