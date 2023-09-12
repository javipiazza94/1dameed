def evaluaedad(edad):
    if edad<23:
        print("Es un zoomer")
    elif edad<38:
        print("Es un milennial")
    elif edad<53:
        print("Es un xennial")
    elif edad<75:
        print("Es un boomer")
    elif edad<110:
        print("Es un post IIGM")

while True:
    try:
        edad = int(input("Introduce la edad del notas: "))
        if edad>0:
            break
        if edad<0:
            print("Las edades negativas son imposibles.")
    except ValueError as EdadNegativa:
        print("Introduce otra")
resultado = evaluaedad(edad)

