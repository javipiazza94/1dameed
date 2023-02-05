#CALIFICA NOTAS
notas = int(input("Dame una nota: ")) #Por defecto en los input  detecta un String. Por eso hay que castearlo previamente
def dameNotas(notas):
    if notas>5 and notas <7:
        print("Aprobado")
    elif notas>=7 and notas <9:
        print("Notable")
    elif notas>=9 and notas <10:
        print("Sobresaliente")
    elif notas==10 :
        print("Matricula de honor")
    elif notas>10:
        print("Nota inexistente")
    else:
        print("Suspendido")
        
dameNotas(notas)

#PIDE EDAD
edad = int(input("Dame una edad: "))
if 0<edad<115:
    print("La edad es correcta")
else:
    print("No existe esa edad")
    
#ORDENA SALARIOS
salario_presidente = int(input("Dame un salario: "))
salario_jefe_area = int(input("Dame un salario: "))
salario_empleado= int(input("Dame un salario: "))

if salario_presidente>salario_jefe_area>salario_empleado:
    print("El salario del presidente es " +str(salario_presidente), " el del jefe de area es " +str(salario_jefe_area), " y el del empleado es " +str(salario_empleado))
else:
    print("La empresa no sabe pagar")

#BECAS
distancia = int(input("Dame la distancia entre la universidad y tu casa: "))
numero_hermanos = int(input("Dame tu numero de hermanos: "))
salario_familia = int(input("Dame tu salario familiar: "))

def calcularBeca(distancia, hermanos, salario):
    beca = 0
    if distancia>20 and hermanos>2 or salario <12000:
        beca = 5000
        print("Tienes derecho a una beca de " +str(beca))
    else:
        print("Te comes un nabo mas gordo que el de Nacho Vidal en su prime")
        
calcularBeca(distancia, numero_hermanos, salario_familia)

lista = ["Agripa", "Caton", "Marco Antonio", "Germanico"]
romano = input("Introduce un romano: ")
# romano.lower() Convierte todo en minuscula
if romano in lista:
    print("acertaste")
else:
    print("No se encuentra")
