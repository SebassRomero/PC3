# Importa el módulo
import operaciones
try:
     numero1= float(input('Ingresar el primer número: '))
     numero2= float(input('Ingresar el segundo número: '))
     resultado_suma = operaciones.suma(numero1, numero2)
     print(f"Suma: {resultado_suma}")

     resultado_resta = operaciones.resta(numero1, numero2)
     print(f"Resta: {resultado_resta}")

     resultado_producto = operaciones.producto(numero1, numero2)
     print(f"Producto: {resultado_producto}")

     resultado_division = operaciones.division(numero1, numero2)
     print(f"División: {resultado_division}")

except ZeroDivisionError:
       print('No es posible dividir entre cero.')
except ValueError:
    print('Ingresar datos numericos')



