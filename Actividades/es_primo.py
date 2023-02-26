def esprimo():
    numero: int = int(input('Introduce un número entero: '))

    if numero > 1:
        for factores in range(2,int(numero)):
            if (int(numero) % factores) == 0:
                print(f"NO ES PRIMO. Es divisible entre {factores}")
                break
            else:
                print(f"EL {numero} ES PRIMO")
    else:
        print(f"{numero} NO ES PRIMO al ser menor que 1")

print({esprimo()})