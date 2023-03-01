import csv

# Abrimos el archivo CSV en modo lectura
with open("ejemplo1.csv", "r") as fichero:
    # Creamos un objeto CSV Reader para leer los datos del archivo
    contenido = csv.reader(fichero)

    # Imprimimos la lista completa de datos
    for row in contenido:
        print("Fila "+str(contenido.line_num)+" "+str(row))

    # Accedemos a datos específicos del archivo
    fichero.seek(0)  # Volvemos al inicio del archivo con el puntero
    contenido = csv.reader(fichero)
    datos = list(contenido)
    print(datos[0][1])
    print(datos[1][0])
    print(datos[2][2])

#Abrimos un archivo mas complejo y nos saltamos la primera linea
fichero2 = open("ejemplo2.csv")
contenido2 = csv.reader(fichero2,quotechar='"')
next(contenido2)
for row in contenido2:
    print(row)

#Creamos y escribimos un csv
fichero3 = open("ejemplo3.csv","w", newline='')
contenido3 = csv.writer(fichero3)
contenido3.writerow(['4/5/2015 13:34', 'Apples', '73'])
contenido3.writerows([['4/5/2015 3:41', 'Cherries', '85'], ['4/6/2015 12:46', 'Pears', '14']])
fichero3.close()

