
cadena = input("Introduce una contraseña: ")
letra = input("Introduce una letra: ")
for iteracion in cadena:
    cadena = cadena.replace(iteracion, letra) #Sustituimos letras
print(cadena)

prueba = input("Introduce una palabra: ")
lista = prueba.split(" ")
for i in lista:
    print(i[2]) #devuelve la tercera letra
    print(i.capitalize()) #pone la primera letra en mayusculas
    print(i.startswith("p")) #te dice si tiene la p de inicio

cad1=input("Cadena:")
if cad1.lower()==cad1[::-1].lower(): #devuelve si se lee igual o no de izquierda a derecha o viceversa
        print("palindromo")
else:
        print("no palindromo")