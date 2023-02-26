from functools import reduce
#Ejecuta la funcion dentro de la lista hasta que se quede con un unico elemento. Necesitan dos parametros
#Genera un unico resultado en la lista, lo hace de manera ciclicamente con cada resultado anterior de a la funcion aplicada a los elementos de la lista
def Suma(x, y):
    print(f'x={x}, y={y}')
    return x+y

lista=[1,2,3,4,5,6,7,8,9]

resultado = reduce(Suma, lista)
print(resultado)

