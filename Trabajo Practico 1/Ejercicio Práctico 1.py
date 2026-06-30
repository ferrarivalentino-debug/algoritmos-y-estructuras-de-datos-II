# Materia: Algoritmos y Estructuras de Datos II
# Alumno/a: Valentino Ferrari
# TP N°: 1 | Ejercicio N°: 1
# Fecha de entrega: 29/6/2026

# Plantilla para otras clases
class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self.marca = marca
        self.velocidad_max = velocidad_max

    def describir(self):
        pass #Se le dara una funcion en las otras clases


#Clases derivadas
class Auto(Vehiculo): #Deriva todo de vehiculo y sobreescribe describir con la informacion apropiada
    def __init__(self, marca, velocidad_max):
        super().__init__(marca, velocidad_max)

    def describir(self):
        return f"El Auto seleccionado es un {self.marca} y su velocidad maxima es de {self.velocidad_max} por hora"

class Moto(Vehiculo): #Lo mismo que en Auto
    def __init__(self, marca, velocidad_max, cillindrada):
        super().__init__(marca, velocidad_max)
        self.cillindrada = cillindrada

    def describir(self):
        return f"La moto seleccionada es una {self.marca} y su velocidad maxima es de {self.velocidad_max} por hora con {self.cillindrada}cc"


#Lista
Elektrowagen = Auto("Flocken", 15)
Corolla_E10 = Auto("Toyota", 170)
Ninja_400 = Moto("Kawasaki", 193, 399)
SR250 = Moto("Yahama", 130, 239)

lista_vehiculos = [Elektrowagen, Corolla_E10, Ninja_400, SR250]

for Vehiculo in lista_vehiculos:
    print(Vehiculo.describir())