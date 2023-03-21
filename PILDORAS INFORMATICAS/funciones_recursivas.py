#Funciones recursivas --> Es una función que se llama a sí misma dentro de su propia definición para resolver un problema.
def Factorial(numero):
    if numero ==0 or numero==1:
        return 1
    else:
        return numero*(Factorial(numero-1)) 

cifra= int(input("Introduce un numero para hacer un factorial: "))
print(Factorial(cifra))

#Funciones lambda --> nos sirven para crear pequeñas funciones anónimas, de una sola línea sobre la marcha.
cifra2= int(input("Introduce un numero para calcular su cuadrado: "))
cuadrado = lambda x: x**2
print(cuadrado(cifra2))

#Decoradores --> Los decoradores son funciones que reciben como parámetros otras funciones y retornan como resultado otras funciones con el objetivo de alterar el funcionamiento original de la función que se pasa como parámetro. 
def tablas(funcion):
    def envoltura(numero=1, tabla=1):
        print('Tabla del %i al %i:' %(tabla, numero))
        print('-' * 15)
        for numero in range(1, numero + 1):            
            funcion(numero, tabla)
        print('-' * 15)
    return envoltura

@tablas
def suma(numero, tabla=1):
    print('%2i + %2i = %3i' %(tabla, numero, tabla+numero))

@tablas
def multiplicar(numero, tabla=1):
    print('%2i X %2i = %3i' %(tabla, numero, tabla*numero))

cifra3= int(input("Introduce un numero para calcular sus tablas de suma y multiplicacion: "))
suma(numero=cifra3)
multiplicar(numero=cifra3)


#Funciones generadoras --> Un generador es un tipo concreto de iterador. Es una función que permite obtener sus resultados paso a paso.
def par(inicio, fin):
    for i in range(inicio, fin):
        if i % 2 == 0:
            yield i

datos = par(1, 5)
print(next(datos))
print(next(datos))

for i in par(20, 30):
    print(i, end=" ")

lista_pares = list(par(1, 10))
print(lista_pares)

#Este código define una función llamada par que utiliza un generador para devolver números pares en un rango dado. 
#Luego, se crean algunos objetos que usan esta función, como un generador llamado datos y una lista llamada lista_pares. Finalmente, se imprimen algunos valores utilizando estos objetos.

