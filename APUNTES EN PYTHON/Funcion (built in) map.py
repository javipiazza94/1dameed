#Funcion map --> Aplica a una funcion a todos los elementos iterables. La diferencia con filter es que la aplica indiscriminadamente a todos los elementos de la lista, y no necesita devolver True o False

def Al_Cuadrado(x):
    return x*x #No necesita devolver True o False. No filtra en la lista
lista = [1,2,3,4,5,6,7,8,9,10]
resultado = map(Al_Cuadrado, lista)
print(list(resultado))