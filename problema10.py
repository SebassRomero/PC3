from problema3 import Circulo
from problema4 import Rectangulo

print("Bienvenido al menú interactivo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Calcular área de un círculo
    2) Calcular área de un rectángulo
    3) Calcular área de un cuadrado
    4) Salir """)
    opcion = input('Ingresar opción: ')

    if opcion == '1':
        try:
            radio = float(input("Ingrese radio para hallar el área del círculo: "))
            mi_circulo = Circulo(radio)
            area = mi_circulo.calcular_area()
            print(f'El área del círculo es: {area}')
            break
        except ValueError:
            print('Ingrese solo valores numéricos')

    elif opcion == '2':
        try:
            largo = float(input("Ingrese el largo para hallar el área del rectángulo: "))
            ancho = float(input("Ingrese el ancho para hallar el área del rectángulo: "))
            mi_recta = Rectangulo(largo, ancho)
            area= mi_recta.area()
            print(f'El área del rectángulo es: {area}')
            break
        except ValueError:
            print('Ingrese solo valores numéricos')

    elif opcion == '3':
        try:
            lado = float(input("Ingrese el lado para hallar el área del cuadrado: "))
            area = lado * lado
            print(f'El área del cuadrado es: {area}')
            break
        except ValueError:
            print('Ingrese solo valores numéricos')

    elif opcion == '4':
        print("Hasta luego")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
