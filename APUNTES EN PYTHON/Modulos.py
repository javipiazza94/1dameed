#Son ficheros en el disco duro que contienen sentencias definidas en un lenguaje de programacion, en este caso es extension .py
    #Se deben de importar para conectarse uno a otro y hacerse referencia. Se usa la sentencia 'import'
    #Un módulo permite organizar lógicamente el código Python. Agrupando código relacionado dentro de un módulo hace el código mas fácil de entender y usar
    # Python tiene modulos preinstalados, como sys, pprint, o math
    #Se recomienda que cada modulo este muy especificado en clases y funciones porque si no se aplicara todo el codigo al importarse
    #Se agrupan en paquetes (contienen modulos y otros paquetes). Son directorios con un fichero especial llamado __init__.py
    #Se pueden anidar paquetes
    
import Funciones # as F --> Sirve para renombrar el nombre del modulo al llamarlo
def main():
    print("Estoy en la funcion main()")
    
if __name__== '__main__':#Estoy implementando la funcion main con un if
    main()

resultado = Funciones.operaciones_matematicas(4,5) #Estoy llamando a una funcion del modulo de Funciones