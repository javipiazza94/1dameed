#funciones

#SUMA POR PARAMETRO DETERMINADO
variable1 = int(input("Introduce un numero "))
variable2 = int(input("Introduce otro numero "))
def suma(a, b):
    return a+b
    
resultado =suma(variable1, variable2)
print(resultado)
    
#SUMA CON ARGUMENTOS INDETERMINADOS
def sumarArgumentos(*args):
    resultado = 0
    for suma in args:
        resultado+=suma
    print(resultado)
lista = [1, 2, 3, 4, 6, 9]   
sumarArgumentos(2, 3, 43, 5, 5)
sumarArgumentos(*lista) #Desempaqueta la lista y suma sus elementos

#FUNCION CON PARAMETROS KEYWORDS INDETERMINADOS
def saludar(nombre = "Javi", **kwargs):
    cadena = nombre
    for valores in kwargs.values():#Recorremos los valores del diccionario
        cadena += " "+valores
    return "Hola "+ cadena

datos = {'nombre' : "Rodolfo", 'apellido' : "Martinez", 'apellido2' : "Hernandez"}
print(saludar(nombre = "Rodolfo", apellido ="Martinez", apellido2 = "Hernandez"))
print(saludar(**datos)) #Metemos los diccionarios de esta manera como parametros indeterminados


