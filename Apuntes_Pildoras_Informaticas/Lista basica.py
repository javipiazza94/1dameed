#Lista

lista = ["Maximo Decimo Meridio", "Cincinato", "Escipion Emiliano", "Craso"]
lista2 = ["Anibal", "Atila", "Arminio"]*2 #Duplicamos valores
lista3 = lista+lista2 #Sumamos las dos listas
print(type(lista)) #Imprimimos el tipo de dato --> devuelve su clase
print(lista) #Imprimimos la lista completa
print(lista[1]) #Imprimimos el indice 1 de la lista
print(lista[1:3]) #Imprimimos un rango de la lista segun los indices. Desde la posicion 0 y el elemento excluido
print(lista[1:]) #Imprimimos desde el elemento 1 hasta el final

#Funciones en las listas
lista.append("Julio Cesar")# para anadir elementos
lista.insert(3, "Marco Antonio")#anadimos un elemento y su posicion
lista.extend(["Adriano", "Trajano", "Ciceron"]) #anadimos otra lista
print(lista.index("Adriano")) #Nos devuelve la posicion del elemento
print(lista)
print("Flavio Aecio" in lista) #devuelve true o false si se encuentra en la lista
lista.remove("Maximo Decimo Meridio")#borramos un elemento
lista.pop()#Borra el ultimo elemento
print(lista)
print(lista3)

LISTA = list(zip(range(1,4),["ana","juan","pepe"])) #FUNCION DE ZIP QUE AGRUPA VARIOS ELEMENTOS
print(LISTA)





