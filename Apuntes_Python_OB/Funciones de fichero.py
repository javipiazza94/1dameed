def escribe(fichero, datos): #Hacemos una funcion con dos parametros: el fichero y los datos a escribir
    f = open(fichero, 'w') #Metemos el comando open con el fichero por parametro y la orden de abrir
    for linea in datos: #Recorremos la lista
        if not linea.endswith('\n'): #Hacemos un if para que nos imprima la lista con los elementos separados
            linea += '\n'
        f.write(linea) #La escribimos
    f.close()

lista = ["\nCayo Octavio Turino ",
        "Cayo Julio Cesar ",          #Esta es la lista a anadir
        "Marco Ulpio Trajano ",
        "Publio Cornelio Escipion El Africano"
        ]
escribe('Fichero para escribir.txt', lista)  #Aplicamos la funcion