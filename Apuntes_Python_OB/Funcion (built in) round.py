#Round --> Redondea al alza o a la baja
#Min --> Devuelve el minimo de una lista
#Max --> Devuelve el maximo de una lista
#sorted --> Devuelve la lista ordenada de menor a mayor
#input --> Pide dato y lo introduce en String (se castea poniendole el tipo(input))
from audioop import reverse
from getpass import getpass

a = 3.6
b = 5.3
lista = (3,6,3,1,2,3,5,8,5,8,56,3,456,9)
al_reves = sorted(lista, reverse=True)
usuario = input("Dime tu usuario")
contrasena = getpass("Dame el passwd")

print(round(a))
print(round(b))
print(min(lista))
print(max(lista))
print(sorted(lista))
print(al_reves)
print(f'El usuario es {usuario} y la contrasena es {contrasena}')