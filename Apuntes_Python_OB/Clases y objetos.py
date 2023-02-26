#Clases y objetos --> Son representaciones de objetos en el mundo real, y tienen sus comportamientos (metodos o funciones de clase) y sus atributos (variables de clase)
    #Son datos de tipo diccionario en el fondo cuya clave (parametro) es el nombre de una funcion. Son azucar sintactico para operar mejor 
    #Toda clase es un objeto
    #Los atributos y metodos no pueden ser privados
class dino:
    encendido = False
    
    def apaga(self):
        self.encendido = False #se coloca el self para referenciar a la variable de clase, si no se esta creando una nueva
    def encender(self):
        self.encendido = True
    def EstaEncendido(self): #Es un get, y referencia la variable de clase (la devuelve)
        return self.encendido

#Para activar la clase tengo que instanciarla (crear un objeto) y de ahi llamar a sus metodos
#Crea una nueva zona de memoria para esa clase, y cada instancia no esta relacionada con la otra y es independiente, solo con la clase (plantilla) 
    #Los objetos se llaman asignando su clase a una nueva variable
        #Los metodos se aplican usando un . entre el objeto y el nombre del metodo
        #No existen los conceptos de public o private o protected en variables de clase, se pueden modificar desde el objeto (todas publicas)
        #Convencion en Python: si una variable o funcion empiezan por _ no se deberia cambiar desde el objeto
Rex = dino()
Rex.apaga()
print(Rex.EstaEncendido())

Rex2 = dino()
Rex2.encender()
print(Rex2.EstaEncendido())

#Clases estaticas
    # Comparten un mismo espacio de memoria y se invocan directamente los metodos sin instanciar. No tienen objetos
    # No tienen self, se pone el mismo nombre de su clase 
    
class estatica():
    numero = 1
    
    def incremento():
        estatica.numero+=1
    def decremento():
        estatica.numero+-1
        
estatica.incremento()
print(estatica.numero) #Imprimimos variable de clase estatica incrementada

#Herencia --> Es la transmision de propiedades y metodos de una clase (padre) a otra clase (hija) para poder ser utilizados. 
                # Se coloca el nombre de la clase padre como parametro en el nombre de la clase hija
                #Puede ser multiple a partir de comas, pero se deberia de evitar
                
class potato(dino):
    nombre = ""
    color = ""
    
    #Metodo constructor con la funcion __init__. Se pone la clase en un valor predeterminado
    #Se instroducen los parametros dentro del init
    #Se activan solo cuando se activa una clase
    def __init__(self, nombre, color):
        print("Estoy en el constructor")
        self.color = "Marron"
        self.nombre = "Don Patata"
        
    def QuitarOreja():
        pass
    def PonerOreja():
        pass
    def __del__(self):
        print("Estoy en el destructor de la clase ", self.__class__)
        #Borra metodos cuando acaba el programa. Lo suele hacer el recolector de basura
    
class Buddy(dino):
    sombrero  = True
    def __init__(self):
        super().__init__()
        print("Estoy en el consturctor de la clase Buddy")
    def QuitarSombrero(self):
        self.sombrero = False
    def PonerSombrero(self):
        self.sombrero
    

Mister = potato("Don Potato", "Negro")
Vaquero = Buddy()
Mister.encender()
print(Mister.EstaEncendido())
#del(Mister) Borra
print(Mister.color)
print(Mister.nombre)
print(Vaquero.QuitarSombrero())
#print(dir(Mister)) # Salen todas las funciones "de regalo" de la clase instanciada



