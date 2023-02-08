limite = int(input("Introduce la cantidad de numeros pares que quieres: "))
def pares(limite):
    num=1
    lista=[]
    while num<limite:
        lista.append(num*2)
        num +=1
    return lista
print(pares(limite))

limite2 = int(input("Introduce la cantidad de numeros pares que quieres: "))
def paresSecuencia(limite2):
    num=1
    while num<limite2:
        yield num*2
        num +=1
devuelve_pares = paresSecuencia(limite2)
for i in devuelve_pares:
    print(i)