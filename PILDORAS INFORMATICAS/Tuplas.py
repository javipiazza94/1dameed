tupla = ("Pepe", 1, 9, 1994)
print(tupla[2])# Posicion de un elemento de la lista
lista =list(tupla) #Convertimos en lista la tupla. Al reves es tuple()
print(lista)
print(tupla)
print( 1 in tupla)#vemos si un elemento esta en la tupla
print(tupla.count(1994)) #vemos cuantas veces se repite un elemento
print(len(tupla)) #indica el numero de elementos

#Desempaquetado de tupla
nombre, dia, mes, ano = tupla #Siempre en este orden y no al reves
print(nombre)
print(dia)
print(mes)
print(ano)
