#Calculadora Python por consola

#Funciones
def suma(num1, num2):
    return num1+num2
def resta(num1, num2):
    return num1-num2
def multiplicacion(num1, num2):
    return num1*num2
def division(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return "Operacion invalida"

#Pedimos datos    
while True:
    try:    
        a = int(input("Introduce el primer numero: "))
        b = int(input("Introduce el segundo numero: "))
        break #Si se introducen correctamente los numeros el bucle se cierra
    except ValueError:
        print("Los valores son incorrectos. Introduce otro de nuevo")
    finally:
        print("Calculo realizado")
operador = input("Introduce un operador (+-*/):")

#Operamos con un switch y las funciones
def realizar_operacion(operador, a, b):
    switch = { #Asociamos el operador a la funcion mediante un diccionario
        '+': suma,
        '-': resta,
        '*': multiplicacion,
        '/': division
    }
    operacion = switch.get(operador) #Obtenemos el operador
    if operacion:
        resultado = operacion(a, b)
    else:
        return "Operador inválido"
    
#Imprimimos resultado
resultado = realizar_operacion(operador, a, b)
print(resultado)
