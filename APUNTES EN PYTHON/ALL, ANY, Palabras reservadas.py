#Sirven para comprobar las condiciones dentro de una lista de elementos

#ANY() --> Comprueba si alguno de los elementos cumple alguna condicion. En caso de que uno solo lo haga dara True, si todos lo incumple da False
lista = [1==1, 2==5, 3==3, 4==4]
resultado = any(lista)
print(resultado)
#any = OR OR OR 

#ALL() --> Comprueba si todos los elementos cumplen la condicion. Si uno da que no, dara False, si todos dan si, dara True
lista2 = [1==1, 2==2, 3==2, 4==4]
resultado2 = all(lista2)
print(resultado2)
#all = and and and

