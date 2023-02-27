#Creamos y escribimos el fichero
f = open("archivo.txt", 'a+')
f.writelines("Viva Franco\n")
f.writelines("Arriba Espana\n")
f.writelines("Una, Grande y Libre\n")
f.close()

#Lo leemos con with que cierra el fichero automaticamente
with open("archivo.txt", 'r') as archivo: 
    #contenido = archivo.read()
    #puntero = archivo.tell()
    #puntero_posicion = archivo.seek(5)
    contenido_lineas = archivo.readlines()
    #print(contenido)
    #print(puntero)
    #print(puntero_posicion)
    print(contenido_lineas)