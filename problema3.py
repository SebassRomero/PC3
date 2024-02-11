import math

class Circulo :
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

if __name__ == "__main__":
    try:
        radio_circulo = float(input("Introduce el radio del círculo: "))
        mi_circulo = Circulo(radio_circulo)
        area_circulo = mi_circulo.calcular_area()
        print(f"El área del círculo con radio {radio_circulo} es: {area_circulo}")
    except ValueError:
        print("Error: Por favor, introduce un valor numérico para el radio del círculo.")