# OPERADORES DE COMPARACION
    #< menor
    #<= menor o igual
    #== exactamente igual
    #> mayor
    #>= mayor o igual
    
#TABLAS DE LA VERDAD
    #AND
print("t y t", True and True)
print("t y f", True and False)
print("f y t", False and True)
print("f y f", False and False)

  #OR 
print("t o t", True or True)
print("t o f", True or False)
print("f o t", False or True)
print("f o f", False or False)

  #XOR
print("t xor t", True ^ True)
print("t xor f", True ^ False)
print("f xor t", False ^ True)
print("f xor f", False ^ False)
    
#DEVOLUCION DE BOOLEANO
a = 6
b = 8
c = 9
resultado1 = a>b
resultado2 = (a>b and resultado1>c)
print(resultado1)
print(resultado2)

#REDUCCIONES DE COMPARACION (lo hace el interprete, este es el proceso interno)
x = 1
y = 2

resultado3 = (x>=1 or y > 8)
resultado3 = (True or False)
Resultado3 = (True)
print(resultado3)

resultado4 = ((x>=1 or y > 8) and y ==7)
resultado4 = ((True or False) and (False))
resultado4 = (True and False)
resultado4 = (False)
print(resultado4)

#SENTENCIA DE COMPARACION
    #IF --> if condicion: (true)
                #acciones
            #elif: anade otra comparacion para ejecutar otra accion
            #else: se ejecuta todo lo demas si no se cumple esa condicion principal
                
z = 8
j = 6
if z==9:
    print("La condicion es TRUE y se ejecuta esta linea de codigo")
elif j>8:
    print("La condicion es TRUE y se ejecuta esta linea de codigo")
else:
    print("Todo el resto de condiciones son FALSE y se ejecuta esta linea")
    
nombres = ("Javier", "Rodolofo", "Hugo")
if "Pepe" not in nombres:
    print("Ese nombre no esta en la lista")
    
#SENTENCIAS DE REPETICION
    #WHILE --> while mientras la condicion sea TRUE:
                #acciones (se repiten 0 o mas veces)

contador = 1
while contador<10:
    print("La linea se ejecuta", contador, "veces")
    contador+=1
    if contador%2==0:
        print("Es par", contador)
    elif contador ==5:
        break
    
    #FOR --> for variable_a_guardar in variable_a_recorrer
             #acciones (se repite segun la longitud de valores de la variable iterada)
             
lista = [1, 2, 3, 4, 5, 6, 7]
longitud = len(lista) #len es una palabra reservada que da el numero de valores de una estructura de datos
tupla = (1, 2, 3, 'a', 'b', 'c')
for variable_guardada in lista:
    print(variable_guardada)
print("la lista tiene ", longitud, "items")
print() #salto de linea

for variable_guardada in tupla:
    print(variable_guardada)

print() #salto de linea

for numero in range(3, 10):
    print(numero)
    
print() #salto de linea

for numero in range(longitud):
    print("Imprimeme el numero actual iterado ", numero)
    if numero == 2:
        print("He encontrado el numero 2")
        break
   
print() #salto de linea
nombre = ("Javier", "Rodolfo", "Pepe")
for seleccion in nombre:
    if seleccion == "Hugo":
        print(seleccion)
        break
else:
    print("no encuentro el nombre")
 
print() #salto de linea 
    #SWITCH --> match valor:
                    #case 1
                        #accion
                    #case 2
                        #accion
semana = "lunes"
match semana:
            case "lunes":
               print("Estamos a lunes") 
            case "martes":
               print("Estamos a martes")