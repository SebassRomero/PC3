class Rectangulo:
    def __init__(self, largo ,ancho) :
        self.largo=largo
        self.ancho=ancho
    def area(self):
        return self.largo*self.ancho
    
if __name__ == "__main__":
    try:
        largo = float(input("Introduce el largo del rectangulo: "))
        ancho = float(input("Introduce el ancho del rectangulo: "))
        mi_rectangulo = Rectangulo(largo,ancho)
        area_recta = mi_rectangulo.area()
        print(f"El área del rectangulo es : {area_recta}")
    except ValueError:
        print("Error: Por favor, introduce un valor numérico.")