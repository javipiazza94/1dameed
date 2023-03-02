# 1) Escribir tres funciones que permitan calcular:

#A) La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#B) La cantidad de horas dadas en segundos, minutos y horas
#C) La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

#A) 
def calcularTiempoSegundos(horas, minutos, segundos):
    return horas*3600+ minutos*60 + segundos

print(calcularTiempoSegundos(34, 23, 29))

#B)
def calcularTiempoHoras(horas, minutos, segundos):
    return segundos/3600 + minutos/60 + horas

print(calcularTiempoHoras(0, 53, 28))

#C) 
def calcularTiempoGlobal(segundos):
    horas = segundos//3600 #Divisiones enteras
    segundos-=horas*3600
    minutos = segundos//60
    segundos-=minutos*60
    return horas, minutos, segundos

print(calcularTiempoGlobal(5678))

# 2) Realiza una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:

# Si recibe un argumento, supone que son segundos y convierte a horas, minutos y segundos.
# Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.

def calcularTiempoRandom(*args):
    if len(args)==1:
        return calcularTiempoGlobal(args[0]) #Es la primera posicion de la tupla
    elif len(args)==3:
        return calcularTiempoSegundos(*args)
    else:
        raise TypeError("Se espera 1 o 3 parámetros")

print(calcularTiempoRandom(2, 4, 45))
print(calcularTiempoRandom(348))

# 3) Queremos hacer una función que añada a una lista los contactos de una agenda. 
# Los contactos se van a guardar en un diccionario, y al menos debe tener el campo de nombre, el campo del teléfono, aunque puede tener más campos. 
# Los datos se irán pidiendo por teclado, se pedirá de antemanos cuantos contactos se van a guardar. Si vamos a guardar más información en el contacto, se irán pidiendo introduciendo campos hasta que introduzcamos el “*”.
#4) Amplía el programa anterior para hacer una función de búsqueda, que reciba un conjunto de parámetros keyword y devuelve los contactos (en una lista) que coincidan con los criterios de búsqueda

def guardar_contacto(lista_agenda, **kwargs):
    contacto = {k.lower(): v for k, v in kwargs.items()} # convertimos los nombres de los campos a minúsculas
    lista_agenda.append(contacto)  # añadimos el diccionario a la lista
    return lista_agenda

def buscar_contacto(lista_agenda, **kwargs):
    lista_aciertos = [] #Creamos la lista de aciertos
    for contacto in lista_agenda: #Recorremos la lista de la agenda
        aciertos = 0 #Inicializa el valor de los aciertos
        for campo, valor in kwargs.items(): #Recorremos el diccionario de búsqueda
            if campo.lower() in contacto and contacto[campo.lower()] == valor: #si coinciden sumamos uno
                aciertos += 1
        if aciertos == len(kwargs): #Si el acierto coincide con la longitud del diccionario lo añadimos
            lista_aciertos.append(contacto)
    return lista_aciertos

def main():
    agenda = []  # abre la lista
    cantidad = int(input("¿Cuántos contactos vas a introducir? "))
    for i in range(cantidad):
        contacto = {}  # abre el diccionario
        contacto["nombre"] = input("Indica el nombre: ")  # introduce los campos
        contacto["telefono"] = input("Indica el teléfono: ")
        campo = input("Introduzca otro campo (* para terminar): ")
        while campo != "*":  # Hasta que no se ponga un asterisco se añade un campo al diccionario
            valor = input("Introduzca valor: ")
            contacto[campo] = valor
            campo = input("Introduzca otro campo (* para terminar): ")
        agenda = guardar_contacto(agenda, **contacto)  # se llama a la función anterior para guardar los contactos
    print(agenda)
    filtro = {}
    campo = input("Introduzca un campo para buscar (* para terminar): ")
    while campo != "*":
        valor = input("Introduzca valor a buscar: ")
        filtro[campo] = valor
        campo = input("Introduzca otro campo a buscar (* para terminar): ")
    print(buscar_contacto(agenda, **filtro))

    
#5). Realizar una función recursiva que reciba una lista y que calcule el producto de los elementos de la lista:

def multiplicar(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista.pop()*multiplicar(lista)   
    
    
if __name__ == '__main__':
    main()
    print(multiplicar([3,4,5])) 

