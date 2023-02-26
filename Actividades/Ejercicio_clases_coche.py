class vehiculo:
    color = "verde"
    ruedas = 4
    puertas = 5
class coche(vehiculo):
    cilindrada = 600
    velocidad = 150
    
Panda = coche()
print("El Panda tiene", Panda.ruedas, "ruedas")
print("El Panda tiene el color", Panda.color)
print("El Panda tiene", Panda.puertas, "puertas")
print("El Panda tiene de cilindrada", Panda.cilindrada)
print("El Panda llega a ", Panda.velocidad, "km/h de velocidad")