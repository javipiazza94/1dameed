#Se calcula con tablas de la verdad de los multiplos de 4, 100 y 400
def es_bisiesto():
    numero: int = int(input('Introduce un año: '))
    if numero % 4 != 0: #no divisible entre 4
        print("No es bisiesto")
    elif numero % 4 == 0 and numero % 100 != 0: #divisible entre 4 y no entre 100 o 400
        print("Es bisiesto")
    elif numero % 4 == 0 and numero % 100 == 0 and numero % 400 != 0: #divisible entre 4 y 10 y no entre 400
        print("No es bisiesto")
    elif numero % 4 == 0 and numero % 100 == 0 and numero % 400 == 0: #divisible entre 4, 100 y 400
        print("Es bisiesto")
    
print({es_bisiesto()})

