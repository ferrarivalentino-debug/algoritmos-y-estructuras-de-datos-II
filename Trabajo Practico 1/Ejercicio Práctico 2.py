# Materia: Algoritmos y Estructuras de Datos II
# Alumno/a: Valentino Ferrari
# TP N°: 1 | Ejercicio N°: 1
# Fecha de entrega: 29/6/2026
import math
#Plantilla
class Figura:
    def __init__(self, color):
        self.color = color

    def describir(self):
        return f"Color: {self.color} - Area: {self.area()}"

#Subclases
class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

lista_figuras = [
    Rectangulo("Amarillo", 2, 4),
    Circulo("Verde", 7)
    ]
print ("Areas!!!")
for figura in lista_figuras:
    print(figura.describir())