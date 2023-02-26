#Crea jerarquias sin utilizar herencia. Consiste en que una clase contiene  1 o mas instancias de otras clases sin heredar metodos.
#En la herencia las clases heredan sus funciones

class motor:
    tipo = "diesel"
class ruedas:
    numero = 4   

class ventana:
    numero = 5
    def cambiarNumero(self, cantidad):
        self.numero = cantidad
    
class carroceria:
    ventana = ventana()

class coche: #Clase que compone a las demas
    motor = motor()
    ruedas = ruedas()
    carroceria = carroceria()
    ventana = ventana()
            
fabia = coche()
print("Motor es", fabia.motor.tipo)
print("Ventanas:", fabia.carroceria.ventana.numero)
fabia.carroceria.ventana.cambiarNumero(6) #invocamos metodo de cambiar ventana con parametro
print("Ventanas:", fabia.carroceria.ventana.numero)