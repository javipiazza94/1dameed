#Clases heredadas
class Persona():
    def __init__(self, nombre, edad, residencia, telefono):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia
        self.telefono = telefono
        
    def descripcion(self):
        print("La persona se llama:", self.nombre, "su edad es:", self.edad, "su residencia está en:", self.residencia, "y su teléfono es:", self.telefono)

class Empleado(Persona):
    def __init__(self, nombre, edad, residencia, telefono, puesto, sueldo, antiguedad):
        super().__init__(nombre, edad, residencia, telefono)
        self.puesto = puesto
        self.sueldo = sueldo
        self.antiguedad = antiguedad
    def descripcion_empleado(self):
        print("El puesto es:", self.puesto,"su salario es:", self.sueldo, "y sus años de antiguedad son:", self.antiguedad)


Antonio = Empleado("Antonio", 35, "Madrid", "123456789", "Director", 60000, 12)
Antonio.descripcion()
Antonio.descripcion_empleado()
print(isinstance(Antonio, Persona))
