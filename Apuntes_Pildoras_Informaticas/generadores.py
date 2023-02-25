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
    
def devuelve_nazis(*nazis): #el * indica que va a recibir un numero indeterminado de elementos por parametro en forma de lista
    for i in nazis:
        #for j in i:
            yield from i
panitas = devuelve_nazis("Goering", "Goth", "Eichmann", "Mengele", "Rommel", "Von Paulus", "Hess", "Goebbels")
print(next(panitas)) #nos devuelve el primer elemento. Con los for anidados nos devuelve el primer elemento de la primera palabra