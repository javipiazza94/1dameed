class alumno:
    def __init__(self, nombre, nota):
        self.nota = nota
        self.nombre = nombre
        
    def datos(self):
        print("La nota del alumno es:", self.nota)
        print("El nombre del alumno es:", self.nombre) 
        
    def EstaAprobado(self):
        if self.nota>=5:
            print("Esta aprobado")
        else: print("Esta suspenso")
        
a1 = alumno("Javi", 7)
a2 = alumno("Jennifer", 4)
a1.datos()
a2.datos()
a1.EstaAprobado()
a2.EstaAprobado()

