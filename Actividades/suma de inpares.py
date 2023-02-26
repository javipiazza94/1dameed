from functools import reduce

lista = (1,2,3,4,5,6,7,8,9)

def InPar(x):
    if x%2!=0:
        return True
    return False
def Suma(x, y):
    return x+y

def Funciones(lista): 
    resultado = list(filter(InPar, lista)) 
    print(resultado)
    resultado = reduce(Suma, resultado) 
    print(resultado)

Funciones(lista)
