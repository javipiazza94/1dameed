import math

def area_triangulo(base, altura):
    return (base*altura)/2
def area_circulo(radio):
    return math.pi * radio ** 2

resultado_triangulo = print("El area del triangulo es ",area_triangulo(23, 76), "cm2")
resultado_circulo = print("El area del circulo es ",area_circulo(23), "cm2")  