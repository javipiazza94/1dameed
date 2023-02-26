from getpass import getpass

Secreto = int(getpass("Introduce el numero secreto a adivinar: "))
valor = 0
while valor!=Secreto:
    valor = int(input("Introduce un numero para adivinar el secreto: "))
    if valor>Secreto:
        print("Es mas bajo")
        continue
    if valor<Secreto:
        print("Es mas alto")
print("Acertaste")