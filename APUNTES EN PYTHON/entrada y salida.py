#Formatear = mostrar variables dentro de una cadena (String)

#Vatiables a mostrar en cadena
numero = 536
texto = "Justiniano"
flotante = 1.2878675

#1* Metodo del Pleistoceno
    #%+d,s o f son los tipos de datos que queremos imprimir. Son placeholders

#print ("El numero es %d, la cadena es %s, y el flotante es %.3f" % (numero, texto, flotante)) #imprime por el orden dado
#print ("el valor de texto es %s" %texto)

#2 Metodo antiguo con la funcion .format() del objeto tipo String
    #Se puede cambiar el orden de las impresiones
    #format se comporta como un array de elementos con sucesivas posiciones de memoria
    
#print ("El numero es {}, la cadena es {}, y el flotante es {}" .format(numero, texto, flotante)) #cada elemento dentro de la llave se guarda en una posicion de memoria 
#print ("El numero es {n1}, la cadena es {s1}, y el flotante es {f1}" #Usamos parametros nombrados para evitar confusiones
#        .format(n1=numero, s1=texto, f1=flotante))

#3Metodo nuevo con f strings --> Hacemos referencia directamente a las variables, ponerles metodos y crear funciones

def suma(a,b):
    return a+b
print(f"El numero es {suma(numero, numero)}, el texto es {texto.upper()} y el flotante es {flotante}")

