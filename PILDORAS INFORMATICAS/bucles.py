# for iterable in ["Rakitic", "Banega", "Kanoute", "Dani Alves"]:
    #print(iterable) #imprimimos el iterable=elemento cuando recorre la lista sin salto de linea

#for iterable in "Supercalifragilisticoespialidoso":
    # print("Viva Franco y Arriba Espana", end=" ")
    
#Creamos un login    
Acceder = False
email = input("Introduce una direccion de email: ")
contrasena = input("Introduce una contrasena: ")
listas = [['javipiazza94@gmail.com', 'Maremaroja94'], 
        ['otro_email@gmail.com', 'otra_contrasena'], #lista de listas
        ['tercer_email@gmail.com', 'tercera_contrasena']]
for usuario, contrasena_registrada in listas: # Metemos dos variables para iterar en la lista
    if (usuario == email) and (contrasena == contrasena_registrada):#Comprobamos que coincidan
        Acceder = True
if Acceder==True:
    print("Accediste")
else:
    print("fallaste")    

#FOR IN RANGE
#for i in range(5, 16, 3): # del 5 al 15 de 3 en 3
    #print(f"el valor de la variable {i}") #Une textos con variables
    
#WHILE
edad = int(input("Introduce tu edad: "))
while edad<0 or edad>100:
    print("Tus muertos, esa edad no existe")
    edad = int(input("Introduce tu edad de nuevo: "))
print(f"Tu edad es {edad}")

#FOR con ZIP
for x,y in zip(range(1,4),["ana","juan","pepe"]):
    print(x,y)