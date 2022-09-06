#Lo hare por dos formas, una hardcodeada y otra por consola y otra con

#hardcodeada
lista = 0
while lista<10:
    lista+=1
    if lista%2!=0:
        print("Los numeros impares de la serie hardcodeada son ", lista)
        
#por consola
numero_inicial: int = int(input('Introduce el número A: '))
numero_final: int = int(input('Inroduce el número B: '))
numeros_impares: int= []

if (numero_inicial<numero_final):
    for variable in range(numero_inicial, numero_final+1):
        if(variable % 2 != 0):
            numeros_impares.append(variable)
else :
    for variable2 in range(numero_final, numero_inicial+1):
        if(variable2 % 2 != 0):
            numeros_impares.append(variable2)

print(f"Los numeros impares entre {numero_inicial} y {numero_final} son:")
print(numeros_impares)