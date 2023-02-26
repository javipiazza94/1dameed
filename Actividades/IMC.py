#Pedimos peso
peso = input("Introduce tu peso en kg ") 
#Pedimos altura
altura = input("Introduce tu estatura en metros ") 
#Hacemos la formula del IMC y calculamos ambas variables en formato float
imc = round(float(peso)/float(altura)**2,2) 
#Imprimimos resultado y lo convertimos a tipo String
print("Tu IMC es " + str(imc))
