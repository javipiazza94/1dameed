#funciones
import math

variable1 = int(input("Introduce un numero "))
variable2 = int(input("Introduce otro numero "))

def suma(a, b):
    return a+b
def resta(a, b):
    return a-b
def multiplicacion(a, b):
    return a*b
def division(a, b):
    return a/b
def exponencia(a, b):
    return a**b
def raiz(a, b):
    return math.sqrt(a) and math.sqrt(b)
    
def raiz(a, b):
    return math.sqrt(a), math.sqrt(b)  # Cambia el 'and' por una coma para obtener ambas raíces

# Realiza las operaciones con las funciones definidas
resultado_suma = suma(variable1, variable2)
resultado_resta = resta(variable1, variable2)
resultado_multiplicacion = multiplicacion(variable1, variable2)
resultado_division = division(variable1, variable2)
resultado_exponencia = exponencia(variable1, variable2)
resultado_raiz_a, resultado_raiz_b = raiz(variable1, variable2)

# Formatea las operaciones y resultados en un mensaje
resultado = f"Las operaciones son:\n\
    Suma: {variable1} + {variable2} = {resultado_suma}\n\
    Resta: {variable1} - {variable2} = {resultado_resta}\n\
    Multiplicacion: {variable1} * {variable2} = {resultado_multiplicacion}\n\
    Division: {variable1} / {variable2} = {resultado_division}\n\
    Exponente: {variable1} ** {variable2} = {resultado_exponencia}\n\
    Raiz: Raiz cuadrada de {variable1} = {resultado_raiz_a}, Raiz cuadrada de {variable2} = {resultado_raiz_b}"

print(resultado)

